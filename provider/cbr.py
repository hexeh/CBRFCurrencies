# -*- coding: utf-8 -*-

import requests
import datetime
import xml.etree.ElementTree as ET

class CBRFetcher:
	def __init__(self, currencies):
		if type(currencies) == list:
			currencies = [c.upper() for c in currencies]
		else:
			raise RuntimeError('currencies must be a list of lowercased char codes')
		dict_request = requests.get('http://www.cbr.ru/scripts/XML_valFull.asp')
		if dict_request.status_code != 200:
			raise RuntimeError('CBR currently unavailable: {0!r}'.format(dict_request.text))
		dict_tree = ET.fromstring(dict_request.text)
		self.dictionary = [{
			'verbose_ru': cur.find('Name').text,
			'verbose_en': cur.find('EngName').text,
			'code': cur.attrib['ID'],
			'iso_num_code': cur.find('ISO_Num_Code').text,
			'iso_char_code': cur.find('ISO_Char_Code').text,
		} for cur in dict_tree.findall('Item')]
		self.currencies = [c for c in self.dictionary if c['iso_char_code'] in currencies]
	def getCurrencyInfo(self, iso_char_code):
		return [c for c in self.dictionary if c['iso_char_code'] == iso_char_code.upper()][0]
	def getCurrenciesInfo(self, all = False):
		if all:
			return self.dictionary
		return self.currencies
	def getExchanges(self, date_range):
		if type(date_range) == list:
			if len(date_range) != 2:
				raise RuntimeError('The date_range parameter should contain only 2 values - start and end date')
			request_date, end_date = date_range
		else:
			request_date = date_range
			end_date = datetime.date.today() - datetime.timedelta(days=1)
		if type(request_date) not in [datetime.date, datetime.datetime] or type(end_date) not in [datetime.date, datetime.datetime]:
			raise RuntimeError('Parameter(s) should have datetime type')
		result = []
		while request_date <= end_date:
			request = requests.get('http://www.cbr.ru/scripts/XML_daily.asp?date_req={0!s}'.format(request_date.strftime('%d/%m/%Y')))
			if request.status_code != 200:
				raise RuntimeError('CBR currently unavailable: {0!r}'.format(request.text))
			currencies_tree = ET.fromstring(request.text)
			for cur in currencies_tree.findall('Valute'):
				result += [{**c,'rate': cur.find('Value').text.replace(',', '.'), 'date': request_date.strftime('%Y-%m-%d')} for c in self.currencies if c['code'] == cur.attrib['ID']]
			request_date += datetime.timedelta(days=1)
		return result
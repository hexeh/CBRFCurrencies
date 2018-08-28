# -*- coding: utf-8 -*-

import pprint
import datetime
from provider import CBRFetcher

if __name__ == '__main__':
	pp = pprint.PrettyPrinter(indent=4)
	# The list of currencies (ISO char codes)
	list_currencies = ['eur','usd','gbp']
	# Initializing instance with the given list
	cbr = CBRFetcher(list_currencies)
	# Print info for specific currency
	pp.pprint(cbr.getCurrencyInfo('usd'))
	# Print info for provided currencies
	pp.pprint(cbr.getCurrenciesInfo())
	# Print exchange rates (for RUB) from given date till yesterday
	simple_date = datetime.date(2018,8,26)
	pp.pprint(cbr.getExchanges(simple_date))
	# Print exchange rates (for RUB) for given date range
	simple_date_range = [datetime.date(2018,8,9),datetime.date(2018,8,10)]
	pp.pprint(cbr.getExchanges(simple_date_range))
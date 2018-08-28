# Курс валют по данным ЦБ РФ
#### Простой класс для получения курса для заданного диапазона дат и списка валют или информации по ним

[Описание](http://www.cbr.ru/development/sxml/)

---

### Инициализация

Для начала работы нужно создать новый экземпляр класса `CBRFetcher` со списком валют, для которых нужно получить курс.

Каждая валюта должна быть представлена своим ISO-кодом (регистр значения не имеет). Пример:

```python
from provider import CBRFetcher

if __name__ == '__main__':
	list_currencies = ['eur','usd','gbp']
	cbr = CBRFetcher(list_currencies)
```

### Получение информации о валютах

Для получения информации по валютам достаточно вызвать метод `getCurrenciesInfo`:

```python
    info = cbr.getCurrenciesInfo(all = False)
```

Параметр `all` отвечает за то, вывести ли информацию обо всех валютах, о которых имеется информация в ЦБ РФ, или только о тех, которые были указаны при создании экземпляра.

Пример выходной информации:

```json
[   {   "code": "R01035",
        "iso_char_code": "GBP",
        "iso_num_code": "826",
        "verbose_en": "British Pound Sterling",
        "verbose_ru": "Фунт стерлингов Соединенного королевства"},
    {   "code": "R01235",
        "iso_char_code": "USD",
        "iso_num_code": "840",
        "verbose_en": "US Dollar",
        "verbose_ru": "Доллар США"},
    {   "code": "R01239",
        "iso_char_code": "EUR",
        "iso_num_code": "978",
        "verbose_en": "Euro",
        "verbose_ru": "Евро"}]
```

Для вывода информации только о какой-то конкретной валюте достаточно вызвать метод `getCurrencyInfo`:

```python
    usd_info = cbr.getCurrencyInfo('usd')
```

Результат:

```json
{   
    "code": "R01235",
    "iso_char_code": "USD",
    "iso_num_code": "840",
    "verbose_en": "US Dollar",
    "verbose_ru": "Доллар США"
}
```

### Получение курса

Для получения курса необходимо вызвать метод `getExchanges` с входным параметром **нужного диапазона дат** - либо __одной даты__ для получения курса по валютам начиная с этой даты и заканчивая вчерашним днем, либо __списка из двух дат__ - даты начала и даты окончания диапазона, для которого нужно получить информацию. В обоих случаях даты должны быть представлены **объектами дат**.

Пример:

```python
    simple_date = datetime.date(2018,8,26)
    exchanges_simple = cbr.getExchanges(simple_date)
    simple_date_range = [datetime.date(2018,8,9),datetime.date(2018,8,10)]
    exchanges_date_range = cbr.getExchanges(simple_date_range)
```

Результат:

```json
{   
    "code": "R01235",
    "date": "2018-08-10",
    "iso_char_code": "USD",
    "iso_num_code": "840",
    "rate": "66.2856",
    "verbose_en": "US Dollar",
    "verbose_ru": "Доллар США"
}
```

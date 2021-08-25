from forex_python.converter import CurrencyRates, CurrencyCodes
from commands import translator

cr = CurrencyRates()
cc = CurrencyCodes()

def currencies():
	codes = cr.get_rates("USD")
	output = []
	for code in codes:
		output.append({
			"code": code,
			"name": cc.get_currency_name(code)
		})
	return output

def languages():
	_langs = translator.get_languages()
	langs = []
	for item in _langs:
		langs.append(item["name"])
	return langs

feature_list = ["Currency conversion", "Translation", "Small talks and Jokes"]
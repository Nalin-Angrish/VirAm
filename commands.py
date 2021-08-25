from forex_python.converter import CurrencyRates, CurrencyCodes
from google.cloud import translate_v2
from argparse import ArgumentParser
import random, difflib, requests

cr = CurrencyRates()
cc = CurrencyCodes()
translator = translate_v2.Client(target_language="en")
JOKE_API_URL = "https://official-joke-api.appspot.com/jokes/general/random"
MEME_API_URL = "https://meme-api.herokuapp.com/gimme"

currency_response_patterns = [
	"{} is equal to {}",
	"{} is the same as {}",
	"{} is {}"
]
translate_response_patterns = [
	"\"{}\" means \"{}\"",
	"\"{}\" is the same as \"{}\"",
	"\"{}\" is \"{}\""
]


def currency(from_currency, from_amount, to_currency):
	try:
		to_value = round(cr.convert(from_currency, to_currency, float(from_amount)), 2)
		return random.choice(currency_response_patterns).format(f"{from_currency} {from_amount}", f'{cc.get_symbol(to_currency)} {to_value}')
	except:
		return "Sorry but I could not convert these currencies. The supported currencies are listed <a href=\"/features/currency\" target=\"_blank\">here</a>."

def translate(*args):
	parser = ArgumentParser()
	parser.add_argument("text", type=str, nargs='+')
	parser.add_argument('--to', nargs="?", default="en", const="en", dest="to_lang")
	_args = parser.parse_args(args)
	_args.text = " ".join(_args.text)
	if len(_args.to_lang) > 2:
		_langs = translator.get_languages()
		langs = []
		codes = []
		for item in _langs:
			langs.append(item["name"])
			codes.append(item["language"])
		this_lang_probs = difflib.get_close_matches(_args.to_lang, langs)
		this_lang = this_lang_probs[0] if len(this_lang_probs) > 0 else "en"   # Set language to english if no close matches were found
		_args.to_lang = codes[langs.index(this_lang)]
	translated_response = translator.translate(_args.text, target_language=_args.to_lang)
	return random.choice(translate_response_patterns).format(translated_response["input"], translated_response["translatedText"])

def get_joke():
	resp = requests.get(JOKE_API_URL).json()[0]
	return f"""<br/>
{resp["setup"]}<br/>
<b>{resp["punchline"]}</b>	
"""
	
def get_meme():
	resp = requests.get(MEME_API_URL).json()
	if resp["nsfw"] is True:
		return get_meme() # Recursively prevent NSFW images
	return f"""<br/>
	<a href="{resp["url"]}" target="_blank"><img src="{resp["url"]}"/></a>
"""
	
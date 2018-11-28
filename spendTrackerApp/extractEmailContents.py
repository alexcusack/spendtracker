import json
import re
from pprint import pprint
from requests_html import HTML

def _extractFields(inputPayload, *args): 
	relevantPayload = dict()
	for key in args:
		print('attempting to extract key', key)
		relevantPayload[key] = inputPayload[key]
	return relevantPayload


def _getChargeString(textBody):
	return textBody.split('\r\n')[4]


def _getDollarsFromString(string):
	return re.findall(r'\d+\.\d+', string)

def _asCents(dollarString):
	return int(round(float(dollarString)*100))

def _getToField(data):
	return data['envelope']['to'].split('@')[0]

def _getSubject(data):
	return data['headers']['Subject'].lower()

def tokenizeFromCloudMailHTML(data): 
	html = HTML(html=data['html'])
	relevantString = html.find('br')[1].text
	vendorName = relevantString.split('at')[1].split('has')[0].strip().lower()
	# print(_getDollarsFromString(relevantString))
	# print(vendorName)
	return {
		'to': _getToField(data), 
		'charge_amount': _asCents(_getDollarsFromString(relevantString)[1]),
		'vendor_name': vendorName,
		'subject': _getSubject(data)
	}

def tokenizeFromCloudMail(data):
	splitBody = data['plain'].split('\n\n')
	chargeString = splitBody[1]
	vendorName = splitBody[1].split('at')[1].split('has')[0].strip().lower()
	return {
		'to': _getToField(data),
		'charge_amount': _asCents(_getDollarsFromString(chargeString)[1]),
		'vendor_name': vendorName,
		'subject': _getSubject(data)
	}





import json
import re
from pprint import pprint

def getCurrentChargeAmount(data):
	relevantPayload = _extractFields(data, 'FromName', 'TextBody')
	chargeString = _getChargeString(relevantPayload['TextBody'])
	chargeAmount = _getChargeAmount(chargeString)
	return _asCents(chargeAmount[0])

def _extractFields(inputPayload, *args): 
	relevantPayload = dict()
	for key in args:
		print('attempting to extract key', key)
		relevantPayload[key] = inputPayload[key]
	return relevantPayload


def _getChargeString(textBody):
	print('text body is:')
	print(textBody)
	return textBody.split('\r\n')[4]


def _getChargeAmount(string):
	return re.findall(r'\d+\.\d+', string)

def _asCents(dollarString):
	return int(round(float(dollarString)*100))


def getCloudMailAmount(data):
	chargeAmount = _getChargeAmount(_getChargeString(data['plain']))
	return _asCents(chargeAmount[0])


def getVendorName(data):	
	message = _getChargeString(data['plain'])
	return message.split('at')[1].split('has')[0].strip().lower()
	# at PACIFIC OCULOFACIAL has 




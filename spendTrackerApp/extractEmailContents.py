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
	return textBody.split('\r\n')[4]


def _getChargeAmount(string):
	return re.findall(r'\d+\.\d+', string)

def _asCents(dollarString):
	return int(round(float(dollarString)*100))




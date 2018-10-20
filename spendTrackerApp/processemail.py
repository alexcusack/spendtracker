import json
import re
from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import logging
from pprint import pprint
from .sendtext import sendText
from .extractEmailContents import (
	tokenizeFromCloudMail
)

from .models import User, Charge

log = logging.getLogger('herokulogs')

@csrf_exempt
def post_handler(request):
	log.info('processing request')
	user = User.lookup_user('6164431505')
	if not user: 
		log.error('no matching user was found')
		return None
	payloadBody = json.loads(request.body.decode('utf-8'))
	print(payloadBody['headers']['Subject'])
	tokenized = tokenizeFromCloudMail(payloadBody)
	charge_amount = tokenized['charge_amount']
	vendor_name = tokenized['vendor_name']
	log.info(f'found charge amount of {charge_amount} from {vendor_name}')
	Charge.save_new_charge(user.first(), charge_amount, vendor_name)
	charges_this_week = Charge.get_charges_since_start_of_week()
	charges_today = Charge.get_charges_since_start_of_day()
	try: 
		text_message = constructTextMessage(charge_amount, charges_this_week, charges_today, vendor_name)
	except Exception as err: 
		log.error(err)
		return HttpResponse(status=404)
	else: 
		log.info('message sent', text_message)
		sendText(text_message, '6164431505')
		return HttpResponse(status=201)


def constructTextMessage(current_charge, charges_this_week, charges_today, vendor_name):
	# fix this: we don't want to return and send a string in the case of not 
	# being able to send a text, else we'll text the error message... :/ 
	if charges_this_week == None or charges_today == None:
		raise Exception("expected charges_this_week and charges_today to be non-null values")
	return """
	
		{current_charge} was just spent @ {vendor_name} 
		{charges_today} so far today. 
		{charges_this_week} so far this week.
	""".format(
			current_charge=formatAsUSD(current_charge),
			charges_today=formatAsUSD(charges_today),
			charges_this_week=formatAsUSD(charges_this_week),
			vendor_name=vendor_name
		)


def formatAsUSD(amount):
	return '${}'.format(amount / 100)




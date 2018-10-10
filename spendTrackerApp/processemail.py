import json
import re
from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import logging
from pprint import pprint
from .sendtext import sendText
from .extractEmailContents import (
	getCurrentChargeAmount
)

from .models import User, Charge

log = logging.getLogger('my thing')

@csrf_exempt
def post_handler(request):
	user = User.lookup_user('6164431505')
	if not user: 
		print('no matching user was found')
		return None
	print('hello', 'world')
	chargeAmount = getCurrentChargeAmount(json.loads(request.body.decode('utf-8')))
	print(f'found charge amount of {chargeAmount}')
	Charge.save_new_charge(user.first(), chargeAmount) # save the new charge amount
	charge_report = Charge.get_sums_by_range()
	text_message = constructTextMessage(charge_report)
	pprint(text_message)
	sendText(text_message, '6164431505')


def constructTextMessage(charge):
	# fix this: we don't want to return and send a string in the case of not 
	# being able to send a text, else we'll text the error message... :/ 
	if charge == None:
		return "Was unable to parse a chage amount from {0}".format(charge)
	return "{charge} was just spent".format(charge=charge)

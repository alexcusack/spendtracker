import re
import json
import logging
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse

from .models import User

log = logging.getLogger(__name__)

@csrf_exempt
def handle_message(request):
	"""Respond to incoming messages with a friendly SMS."""	
	log.info('processing inbound text message')
	try: 
		params = request.POST
		phone = re.sub('\+1','',params['From'])
		message = params['Body']
		if message.strip().lower() == 'signup':
			create_user(phone)
		reply = get_reply_string(request.POST)
		return HttpResponse(create_twilio_reply(reply))
	except Exception as e:
		log.info('error processing inboudn text message', exc_info=True)
		log.info("params were ---> {0}".format(params))
		return HttpResponseBadRequest()



message_to_reply = {
	'default': "Would you like to signup to recieve spending alerts? Reply with 'signup'",

	'signup': """You\'re signed up!
		Configure to send alerts to:
		{phone}@spndtrckr.com
		Instructions: https://github.com/alexcusack/spendtracker/blob/master/README.md
		"""
}


def get_reply_string(params):
	from_phone = re.sub('\+1','',params['From'])
	message = params['Body'].strip().lower()
	interpolable_args = {
		'phone': from_phone
	}
	return message_to_reply.get(message, message_to_reply.get('default')).format(**interpolable_args)


def create_twilio_reply(message_str):
	resp = MessagingResponse()
	resp.message(message_str)
	return str(resp)


def create_user(phone_number):
	user, was_created = User.objects.get_or_create(
		phone_number=re.sub('\+1','', phone_number)
	)
	return user

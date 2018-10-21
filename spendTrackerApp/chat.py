import json
import re
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse

from .models import User


@csrf_exempt
def handle_message(request):
	"""Respond to incoming messages with a friendly SMS."""	
	params = request.POST
	phone = re.sub('\+1','',params['From'])
	message = params['Body']
	if message.strip().lower() == 'signup':
		create_user(phone)
	reply = get_reply_string(request.POST)
	return HttpResponse(create_twilio_reply(reply))



message_to_reply = {
	'default': "Would you like to signup to recieve spending alerts? Reply with 'signup'",

	'signup': """You\'re signed up!
		Configure your chase email alerts to be sent to
		{phone}@spndtrckr.com
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

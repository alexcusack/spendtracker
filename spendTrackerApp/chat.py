import json
import re
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse



@csrf_exempt
def handle_message(request):
	"""Respond to incoming messages with a friendly SMS."""	
	params = request.POST
	phone = re.sub('\+1','',params['From'])
	message = params['Body']
	reply = get_reply(request.POST)
	resp = MessagingResponse()
	resp.message(reply)
	return HttpResponse(str(resp))



message_to_reply = {
	'default': "Would you like to signup to recieve spending alerts? Reply with 'signup'",

	'signup': """You\'re signed up!
		Configure your chase email alerts to be sent to
		{phone}@spndtrckr.com
		"""
}


def get_reply(params):
	from_phone = re.sub('\+1','',params['From'])
	message = params['Body'].strip().lower()
	interpolable_args = {
		'phone': from_phone
	}
	return message_to_reply.get(message, message_to_reply.get('default')).format(**interpolable_args)

import os
from twilio.rest import Client

account_sid = os.environ.get('twilio_account_sid')
auth_token = os.environ.get('twilio_auth_token')
client = Client(account_sid, auth_token)


def sendText(message, phone):
	return client.messages.create(
		body=message,
		from_='+16162293185',
		to=phone
	)
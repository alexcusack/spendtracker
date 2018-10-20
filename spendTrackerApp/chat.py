from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse



@csrf_exempt
def handle_message(request):
	"""Respond to incoming messages with a friendly SMS."""
	    # Start our TwiML response
	resp = MessagingResponse()

    # Add a text message
	msg = resp.message("Would you like to signup to recieve spending alerts? Reply with 'signup'")

    # Add a picture message
    # msg.media("https://demo.twilio.com/owl.png")

	return HttpResponse(str(resp))



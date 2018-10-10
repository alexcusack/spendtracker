from django.http import HttpResponse
from datetime import datetime
import json as simplejson
from django.views.decorators.csrf import csrf_exempt


def ping(request): 
	"""
	Returns an HTTP response with a variety of health check data
	"""
	payload = {
		'pong': True,
		'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	}
	return HttpResponse(simplejson.dumps(payload))

@csrf_exempt
def postPing(request):
	return HttpResponse('you sent a post request and it worked\n')
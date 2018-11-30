#Django Response
from django.http import HttpResponse, JsonResponse
#Utilities:Datetime hora de servidor
from datetime import datetime
import json

def hello_world(request):
	"""Return a greetings"""
	now = datetime.now().strftime('%b %dth %Y - %H:%M hrs')
	return HttpResponse('Oh, hi! Current server time is {now}'.format(now=now))


def hi(request):
	"""Hi"""
	#http://127.0.0.1:8000/hi/?numbers=13,32,50,22
	#PDB es un debuger
	#import pdb; pdb.set_trace()
	numbers = [int(i) for i in request.GET['numbers'].split(',')]
	sorted_ints = sorted(numbers)
	data = {
		'status':'ok',
		'numbers':sorted_ints,
		'message':'Integers sorted successfully.'
	}
	return HttpResponse(json.dumps(data, indent=4), content_type='application/json')

"""
Podemos tener acceso desde el debuger al request y sus metodos:
-META
-GET
-PATH
Etc

"""

def say_hi(request, name, age):
	"""Return a greeting"""
	#http://127.0.0.1:8000/say_hi/Will/22/
	if age<12:
		message = 'Sorry {}, you are not allowed here'.format(name)
	else:
		message = 'Hello, {} welcome to Platzigram'.format(name)
	return HttpResponse(message)
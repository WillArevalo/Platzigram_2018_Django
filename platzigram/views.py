#Django Response
from django.http import HttpResponse, JsonResponse
#Utilities:Datetime hora de servidor
from datetime import datetime

def hello_world(request):
	"""Return a greetings"""
	now = datetime.now().strftime('%b %dth %Y - %H:%M hrs')
	return HttpResponse('Oh, hi! Current server time is {now}'.format(now=now))


def hi(request):
	"""Hi"""
	#PDB es un debuger
	#import pdb; pdb.set_trace()
	numbers = request.GET['numbers'].split(',')
	numbers = [int(i) for i in numbers]
	numbers.sort()
	return JsonResponse({'numbers':numbers})



"""
Podemos tener acceso desde el debuger al request y sus metodos:
-META
-GET
-PATH
Etc
"""
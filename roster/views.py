from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
	context = {
		'message': 'Enough is enough! I\'ve had it with these motherfuckin  snakes on this motherfuckin plane!'
	}
	return render(request,'base.html',context)

from django.shortcuts import render
from django.http import HttpResponse

import requests

# Create your views here.

def submitPage(request):
	context = {}

	return render(request, "messageform.html", context)

def sendMessage(request):
	
	postVals = {
				"bot_id" : "70564e0fc3408c80f6a112ae07",
				}

	postVals["text"] = "Hello."

	return HttpResponse()

def receiveMessage(request):

	return HttpResponse()
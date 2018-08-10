# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from fyleRestApi.models import IndianBanks
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
import json

# Create your views here.

def getBankDetailsFromIFSC(request):
	if request.method == 'GET':
		if 'ifsc' in request.GET:
			ifsc_code=request.GET['ifsc'].upper()
			details=IndianBanks.objects.filter(ifsc=ifsc_code).values()
			if not list(details):
				return HttpResponse("We could not locate any branch with the follwing ifsc code: "+ifsc_code)	
				
			else:
				data=json.dumps(list(details),cls=DjangoJSONEncoder)
				return HttpResponse(data)
		else:
			return HttpResponse("Provide ifsc code to locate your branch!")	

def getBankDetailsFromBankNameAndCity(request):
	if request.method == 'GET':
		if 'bank_name' in request.GET:
			if 'city' in request.GET:
				bank_name=request.GET['bank_name'].upper()
				city=request.GET['city'].upper()
				details=IndianBanks.objects.filter(bank_name=bank_name,city=city).values()
				if not list(details):
					return HttpResponse(" We could not locate any branch with the following city and bank name provided: "+bank_name+","+city )
				else:
					data=json.dumps(list(details),cls=DjangoJSONEncoder)
					return HttpResponse(data)
			else:
				return HttpResponse("Provide the city to locate your branch!")
		else:
			return HttpResponse("Provide the Bank Name to locate your branch!")			
	else:
		return HttpResponse("method not allowed!")		


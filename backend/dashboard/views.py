from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
import requests
from dashboard import price_helper

#def topSentiments(request, param:str):
#    return getSentiment()
    #to-do add address and time as param, but this is good enough for MVP

#def singleCollection(request, param:str):
#    return JsonResponse(price_helper.tokenTrades(request)

#def predict(request, param:str):

def topRank(request, param:str):
    return JsonResponse(price_helper.get_top(partham, 10))
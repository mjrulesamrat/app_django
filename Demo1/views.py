from django.shortcuts import render
import json

# Create your views here.

def post(request):
    mydata = json.loads(request.body)
    
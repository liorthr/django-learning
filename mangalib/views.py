from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import datetime

def index(request):
    context = {
        "message": 'Hello World ! ', 
        'sentence': 'This is a test to fix my issue '       
               }
    template = loader.get_template('mangalib/index.html')
    return HttpResponse(template.render(context, request))
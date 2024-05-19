from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    context = {
        "message": 'Hello World ! ',
        'message2': 'Juste un test'            
               }
    template = loader.get_template('mangalib/index.html')
    return HttpResponse(template.render(context, request))
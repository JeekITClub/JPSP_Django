from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):
    return HttpResponse("A website.")
def club_fileupload(request):
    return HttpResponse("file")
def admin_login(request):
    template=loader.get_template('admin/login.html')
    content={

    }
    return HttpResponse(template.render(content,request))

def login(request):
    template=loader.get_template('')
    content={

    }
    return HttpResponse(template.render(content,request))




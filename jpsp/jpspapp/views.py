from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):
    template=loader.get_template('index.html')
    content={}
    return HttpResponse(template.render(content,request))
def club_admin_file(request):
    template=loader.get_template('club/admin/file.html')
    content={}
    return HttpResponse(template.render(content,request))
def admin_login(request):
    template=loader.get_template('admin/login.html')
    content={}
    return HttpResponse(template.render(content,request))
def login(request):
    template=loader.get_template('login.html')
    content={}
    return HttpResponse(template.render(content,request))

# TODO: file request and save




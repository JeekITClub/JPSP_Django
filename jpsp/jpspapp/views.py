from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import os

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    content = {}
    return HttpResponse(template.render(content, request))


def admin(request):
    template=loader.get_template('admin/index.html')
    content={"username":"hello"}
    return HttpResponse(template.render(content,request))

def admin_login(request):
    template = loader.get_template('admin/login.html')
    content = {}
    return HttpResponse(template.render(content, request))

def register(request):
    template = loader.get_template('register.html')
    content = {}
    return HttpResponse(template.render(content,request))

def login(request):
    template = loader.get_template('login.html')
    content = {}
    return HttpResponse(template.render(content, request))

def club_admin_file(request):
    template = loader.get_template('club/admin/file.html')
    content = {}
    return HttpResponse(template.render(content, request))


def club_admin_file_upload(request):
    if request.method == 'POST':
        file=request.FILES.get("file",None)
        def handle_uploaded_file(f):
            destination=open(os.path.join(r"D:/upload",f.name),'wb+')
            for chunk in file.chunks():
                destination.write(chunk)
            destination.close()
        if file:
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("hello")
        else:
            return HttpResponse("no file for upload!")
    else:
        template = loader.get_template('login.html')
        content = {}
        return HttpResponse("sorry")
        # from django.core.files.base import ContentFile
        # from django.core.files.storage import get_storage_class
        #
        # storageSystem = get_storage_class()('/Absolute/path/to/save/file')
        # the_file = ContentFile(content="#Hello world!"，name = "Hello.md")
        # storageSystem.save(content=the_file

# TODO: Finish the club_admin_file_upload

def club_all(request):
    template = loader.get_template('club/club_all.html')
    content = {}
    return HttpResponse(template.render(content,request))

def clubid(request):
    template = loader.get_template('club/clubid/index.html')
    content = {}
    return HttpResponse(template.render(content,request))

def test(request):
    template = loader.get_template('')
    content = {}
    return HttpResponse(template.render(content,request))
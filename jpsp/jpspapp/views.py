from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
import os

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    content = {}
    return HttpResponse(template.render(content, request))


def club_admin_file(request):
    template = loader.get_template('club/admin/file.html')
    content = {}
    return HttpResponse(template.render(content, request))


def admin_login(request):
    template = loader.get_template('admin/login.html')
    content = {}
    return HttpResponse(template.render(content, request))


def login(request):
    template = loader.get_template('login.html')
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


# TODO: Finish the club_admin_file_upload
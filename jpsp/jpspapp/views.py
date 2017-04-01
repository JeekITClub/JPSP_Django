from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .forms import UploadFileForm
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
def club_admin_file_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        def handle_uploaded_file(f):
            with open('files', 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
        template=loader.get_template('login.html')
        content={}
        return HttpResponse(template.render(content,request))
# TODO: file request and save




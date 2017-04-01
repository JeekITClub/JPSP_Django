from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("A website.")
def club_fileupload(request):
    return HttpResponse("file")

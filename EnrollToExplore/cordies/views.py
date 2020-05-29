from django.shortcuts import render, HttpResponse, redirect, reverse
from .forms import *
# Create your views here.
def contacts(request):
	return render(request,'contacts.html')


def base(request):
	return render(request,'base.html')



def schedule(request):
	return render(request,'schedule.html')


def error_404_view(request, exception):
	return render(request,'error404.html')
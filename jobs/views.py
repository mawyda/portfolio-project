from django.shortcuts import render

from .models import Job # import the Jobs model
# Create your views here.

def home(request):
	jobs = Job.objects 
	return render(request, 'jobs\home.html', {'jobs': jobs})

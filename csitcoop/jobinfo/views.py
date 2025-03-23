from django.shortcuts import render,get_object_or_404
from main.models import *

def info(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'info.html', {"job": job})

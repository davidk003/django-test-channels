from django.shortcuts import render
from django.http import HttpResponse
import random, time


jobs = {}


def my_view(request):
    return HttpResponse("Hello, world!")


def run_job(request):
    job_id = random.randint(0, 1000)
    if job_id in jobs:
        return HttpResponse("Job already running or job_id generated already in use")
    jobs[job_id] = True
    time.sleep(10)
    jobs[job_id] = False
    del jobs[job_id]
    return HttpResponse("Job done.")

def check_jobs(request):
    return HttpResponse(str(jobs))
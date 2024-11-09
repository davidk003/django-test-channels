from django.shortcuts import render
from django.http import HttpResponse
import random, time
from channels.layers import get_channel_layer



jobs = {}


def my_view(request):
    return HttpResponse("Hello, world!")


def run_job(request):
    job_id = random.randint(0, 1000)
    if job_id in jobs:
        return HttpResponse("Job already running or job_id generated already in use")
    jobs[job_id] = True
    for i in range(10):
        time.sleep(1)
        send_progress_update(f"{(i/10)*100}% completed") 
    jobs[job_id] = False
    del jobs[job_id]
    return HttpResponse("Job done.")

def check_jobs(request):
    return HttpResponse(str(jobs))

async def send_progress_update(message):
    channel_layer = get_channel_layer()
    channel_layer.group_send(
        "progress",  # group name
        {
            "type": "progress_update",  # matches the method name in the consumer
            "message": message,  # message content to send
        }
    )
# jobRunner/urls.py
from django.urls import path
from jobRunner.views import *


urlpatterns = [
    path('my_view/', my_view),
    path('run_job/', run_job),
    path('check_jobs/', check_jobs),
]
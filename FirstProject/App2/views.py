from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
import datetime;
def f22(request):
    time=datetime.datetime.now();
    msg="<h2>Hello User....!!<br/><br/>Server date & Time ::"+str(time)+"</h2><hr/>"
    return HttpResponse(msg);
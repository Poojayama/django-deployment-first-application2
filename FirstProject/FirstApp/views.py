from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def display(request):
    print("Welcome/ url is requested & display() is Executed")
    ss='''
    <center>
    <h2 style="color:Blue;">
    Hello User,Welcome to Django First-Project FirstApp
    </h2>
    </center>
    ''';
    return HttpResponse(ss);


def show(request):
    ss='''
        <html>
        <head>
        <title>***Welcome-Page</title>
            <style>
                h1{
                color:Blue;
                }
                h2{
                color:Green;
                }
                h3{
                color:white;
                }
                h4{
                color:violet;
                }
                h1,h3,h5{
                    background-color:red;
                    border:2px Solid Brown;
                    }
                h2,h4,h6{
                    background-color:yellow;
                    border:2px Solid Brown;
            </style>
        </head>
            <body>
                <center>
                    <h1>Welcome to DJANGO HTML webpage</h1>
                    <hr color="brown" width="95%"/>
                    <h2>Welcome to DJANGO HTML webpage</h2>
                    <hr color="brown" width="85%"/>
                    <h3>Welcome to DJANGO HTML webpage</h3>
                    <hr color="brown" width="75%"/>
                    <h4>Welcome to DJANGO HTML webpage</h4>
                    <hr color="brown" width="65%"/>
                    <h5>Welcome to DJANGO HTML webpage</h5>
                    <hr color="brown" width="55%"/>
                    <h6>Welcome to DJANGO HTML webpage</h6>
                    <hr color="brown" width="45%"/>
                </center>
            </body>
        </html>
    '''
    return HttpResponse(ss);
    
def hello(request):
    print("hello/ url is requested & display() is Executed")
    ss='''
        <html>
        <head>
            <title>Hello Webpage</title>
            <style>
                h1{
                color:Blue;
                width:90%;
                }
                h2{
                color:Green;
                Width:80%;
                }
                h3{
                color:white;
                width:70%;
                }
                h4{
                color:violet;
                width:60%;
                }
                h1,h3,h5{
                    background-color:lightblue;
                    border:2px Solid Brown;
                    }
            </style>
        </head>
        <body>
            <center>
                <h1>Hello User....!!!</h1>
                <hr color='brown' width='80%'/>
                <h2>Welcome to Django-App</h2>
                <hr color='brown' width='80%'/>
                <h3>Have a nice day...</h3>
                <hr color='brown' width='80%'/>
            </center>   
        </body>
        </html>
    '''
    return HttpResponse(ss);
 
import time;
def senddatetime(request):
    print("dtime/ url is requested & senddatetime() is executed");
    ct=time.ctime()
    print("Client Request date & time on server ::",ct);
    ss='''
    <html>
        <head>
            <title>Date-time Webpage</title>
            <style>
                h1{
                    color:Blue;
                    width:90%;
                    }
                h2{
                    color:Green;
                    Width:80%;
                    }
                h3{
                    color:white;
                    width:70%;
                    }
                h4{
                    color:violet;
                    width:60%;
                    }
                h1,h3,h5{
                        background-color:lightblue;
                        border:2px Solid Brown;
                        }                
            </style>
        </head>
        <body>
            <center>
                <h1>welcome to Django-User...!!!</h1>
                <hr color='brown' width='80%'/>
                <h2> Server-Date & Time ::</h2>
                <hr color='brown' width='70%'/>
                <h3>''',ct,'''</h3>
                <hr color='brown' width='60%'/>
            </center>
        </body>
    </html>
    ''';
    return HttpResponse(ss);    

#Single view and multiple-urls
def demo(request):    
    print("mulitiple-Request-URLs same response");
    htmldata='''<center>
        <h1>Welcome demo User!!!</h1>
        <hr/>
        <h2> This is same-output for diff-multiple-Requests-Urls</h2>
        <hr/>
        <h3>Have a Great day...</h3>
        </center>''';
    return HttpResponse(htmldata); 
#default-url-request-view-func-Homepage
def homepage(request):
        htmldata='''<center>
            <h1>welcome to Default Home-Page!!!</h1>
            <hr/>
            <h2>Your Request Page is Not-Found...</h2>
            <hr/>
            <h3>Plz try other URL or Links!!!</h3>    
        </center>''';
        return HttpResponse(htmldata);    
from django.shortcuts import render
from django.http import HttpResponse
from . import models
import smtplib
import random
import math

def login(request):
    return render (request,'quizsys/login.html')
def home(request):
    return render(request,'quizsys/home.html')
def regs(request):
    return render(request,'quizsys/regs.html')
def result(request):
    return render(request,"quizsys/result.html")
def start(request):
    return render(request,"quizsys/start.html")

def quizpage(request):
    res=models.getData()
    return render (request,'quizsys/quizpage.html',{"out":res})

def nextques(request):
    id=int(request.GET['id'])+1
    if id<=4:
        res=models.editques(str(id))
        return render(request,"quizsys/quizpage.html",{"out":res})
    else:
        id=1
        res=models.editques(str(id))
        return render(request,"quizsys/quizpage.html",{"out":res})

def backques(request):
    id=int(request.GET['id'])-1
    if id>0:
         res=models.editques(str(id))
         return render(request,"quizsys/quizpage.html",{"out":res})
    else:
        id=1
        res=models.editques(str(id))
        return render(request,"quizsys/quizpage.html",{"out":res})
        

    
from django.http import HttpResponse
from django.shortcuts import render
import joblib


def home (request):
    return render(request,"index.html")


def result(request):

    cls = joblib.load('randomforest_model.sav')
    lis = []
   
    lis.append(request.GET['Age'])
    lis.append(request.GET['Experience'])
    lis.append(request.GET['Income'])
    lis.append(request.GET['Family'])
    lis.append(request.GET['CCAvg'])
    lis.append(request.GET['Education'])
    lis.append(request.GET['Mortgage'])
    lis.append(request.GET['Securities Account'])
    lis.append(request.GET['CD Account'])
    lis.append(request.GET['Online'])
    lis.append(request.GET['CreditCard'])
    
    ans = cls.predict([lis])

    


    return render(request,"result.html",{'ans':ans,'lis':lis})
   

    

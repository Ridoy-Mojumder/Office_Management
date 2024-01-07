from django.shortcuts import redirect,render
from django.http import HttpResponse
from myApp.models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.shortcuts import get_object_or_404

import random


def singupPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        displayName=request.POST.get('displayName')
        email=request.POST.get('email')
        password=request.POST.get('password')
        job_type=request.POST.get('jobType')


        user=Office_User.objects.create_user(username=username,password=password)

        user.display_name=displayName
        user.email=email
        user.job_type=job_type
        user.save()
        if user.job_type=="office_manage":
            user=Office_Manager_Profile.objects.create(user=user)
            user.save()

        if user.job_type=="administrative_assistant":
            user=Administrative_Assistant_Profile.objects.create(user=user)
            user.save()

        
        if user.job_type=="executive_assistant":
            user=Executive_Assistant_Profile.objects.create(user=user)
            user.save()



        if user.job_type=="receptionist":
            user=Receptionist_Profile.objects.create(user=user)
            user.save()


        return redirect("singinPage")

    return render(request,"signup.html")



def singinPage(request):
    myMessage={
        "error_message":"user not found",
        "success_message":"Login successfully" 
    }
    
    if request.method =='POST':
        user_name=request.POST.get("username")
        myPass=request.POST.get("password")
        
        print(user_name,myPass)
        
        user=authenticate(request,username=user_name,password=myPass)

        print(user)

        if user is not None:
            login(request,user)
            return redirect("deshboardPage")
        else:
            messages.warning(request,myMessage["error_message"])
        
        
    return render(request,'login.html')


def logoutPage(request):
    logout(request)
    return redirect("singinPage")

@login_required
def deshboardPage(request):
    return render(request,"deshboard.html")





        
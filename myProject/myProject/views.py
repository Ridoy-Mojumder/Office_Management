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


@login_required
def profilePage(request):

    return render(request,"profile.html")

@login_required
def view_taskPage(request):
    task=task_model.objects.all()
    return render(request,'view_task.html',{'task':task})


@login_required
def add_taskPage(request):

    user=request.user


    if request.method == "POST":
        taskTitle=request.POST.get('task_title')
        task_description=request.POST.get('task_description')
        p_pic=request.FILES.get("profilePicture")

        task=task_model(
            task_title=taskTitle,
            task_description=task_description,
            Profile_Pic=p_pic,
            task_creator=user,
        )
        

        task.save()
        return redirect("view_taskPage")

    return render(request,"add_task.html")

@login_required
def delete_taskPage(request,myid):

    task=task_model.objects.filter(id=myid)
    task.delete()
    return redirect("view_taskPage")

@login_required
def edit_taskPage(request,myid):

    task=task_model.objects.filter(id=myid)

    return render(request,"edit_task.html",{'job':task})

@login_required
def update_taskPage(request):
    
    user=request.user


    if request.method == "POST":
        id=request.POST.get('task_id')
        taskTitle=request.POST.get('task_Title')
        description=request.POST.get('task_description')
        p_pic=request.FILES.get("profilePicture")

        job=task_model(
            id=id,
            task_title=taskTitle,
            task_description=description,
            task_creator=user,
            Profile_Pic= p_pic,
        )
        job.save()
        return redirect("view_taskPage")



@login_required
def message_Page(request):

    return render(request,"message.html")

@login_required
def contactUs_Page(request):

    return render(request,"contact_us.html")

@login_required
def view_team_member_page(request):
    user= request.user
    creator=Office_User.objects.filter(username=user)
    return render(request,"view_team_member.html",{'creator':creator})

@login_required
def view_team_member_page(request):
    team_member=Office_User.objects.all()
    complex={
        'view_team_member':team_member
    }
    return render(request,'view_team_member.html',complex)
        
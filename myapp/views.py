from urllib import request
from django.shortcuts import redirect, render, HttpResponse, HttpResponseRedirect
from django import template
from django.template import loader
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login , logout as auth_logout



# Create your views here.

#To go to Home page 

def home(request):
    return render(request, 'Home.html')

#To let login user 
def Login(request):
    #If user already log in
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        User_name = request.POST['User_name']
        user_pass=request.POST['user_pass']
        print(user_pass)
        user = authenticate(request, username=User_name, password=user_pass)
        print(user)
        if user is not None:
            auth_login(request, user)
            messages.success(request,"You are now logged in")
            return redirect('/')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/Login')
    return render(request, 'login.html')


#To let ragistered user 
def ragi(request):
    #If user already log in
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        Username = request.POST['Username']
        Email = request.POST['Email']
        Password = request.POST['Password']
        confirm_pass = request.POST['confirm_pass']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']

        #To check user already ragistered or not
        number_check = User.objects.filter(username=Username).exists()
        email_check = User.objects.filter(email=Email).exists()

        #If user already exist
        if number_check == True:
            messages.error(request,"Your Username  Already Exists")
            return redirect('/Login')
        if email_check == True:
            messages.error(request,"Your Email Already Exists")
            return redirect('/Login')
        
        if Password != confirm_pass:
            messages.error(request, "Passwords do not match")
            return redirect('/ragi')
        else:
            user = User.objects.create(username=Username, email=Email, password=confirm_pass)
            user.first_name= first_name
            user.last_name = last_name
            user.set_password(confirm_pass)  # Hash the password #It's very-very imp
            user.save()
            messages.success(request, "Your Account Successfully Created")
            return redirect('/Login')
    return render(request, 'ragi.html')

#For logout
def logout(request):
    try:
        auth_logout(request)
        messages.info(request, "Logged out successfully!")
        print("LOG OUT")
        return redirect('Login')

    except Exception as e:
        print("Error during logout:", str(e))
    return redirect('Home')

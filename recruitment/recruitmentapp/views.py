from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import logout
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection

# Create your views here.

def index(request):
    return render(request, 'index.html')

def body(request):
    return render(request, 'body.html')

def job(request):
    return render(request, 'job.html')

def about(request):
    return render(request, 'about.html')

def home(request):
    loggedin = request.session.get('name')
    if loggedin is None:                 # if not logged in  
        return redirect('loginpage') 
    else:
        return render(request, 'home.html')

def loginpage(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            candidate = Candidate.objects.get(email=email)
            if password == candidate.password:
                name=candidate.name
                request.session['name'] = name
                return render(request, 'home.html', {'name': name})  
            else:
                message = "Invalid Password!"
                return render(request, 'login.html', {'message': message})        
        except ObjectDoesNotExist:
            message = "User does not exist!!"
            return render(request, 'login.html', {'message': message})
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        qualification = request.POST['qualification']

        try:
            # Try to fetch a Candidate with the provided email
            existing_candidate = Candidate.objects.get(email=email)
            message = "Email already exists. Please use a different email."
            return render(request, 'register.html', {'message': message})

        except ObjectDoesNotExist:
            # If no Candidate with the provided email exists, create and save a new Candidate
            candidate = Candidate(name=name, email=email, password=password, qualification=qualification)
            candidate.save()
            return redirect('loginpage')  # Redirect to the login page after successful registration
    return render(request, 'register.html')


def logoutpage(request):
    loggedin = request.session.get('name')
    if loggedin is None:                 #not logged in  
        return redirect('loginpage') 
    else:
        if 'username' in request.session:
            del request.session['username']

            logout(request)
            return redirect('loginpage') 
    logout(request)
    return redirect('body') 

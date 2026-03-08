from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Student


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('home')

    return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid Credentials'})

    return render(request, 'login.html')


@login_required
def dashboard(request):
    try:
        student = Student.objects.get(user=request.user)

        if student.cgpa >= 8.5:
            category = "Dream Company"
        elif student.cgpa >= 7:
            category = "Super Dream Company"
        else:
            category = "Mass Recruiter"

    except Student.DoesNotExist:
        student = None
        category = None

    return render(request, 'dashboard.html', {
        'student': student,
        'category': category
    })


@login_required
def create_profile(request):
    if request.method == 'POST':
        branch = request.POST['branch']
        cgpa = request.POST['cgpa']
        skills = request.POST['skills']
        backlog = request.POST['backlog']

        Student.objects.create(
            user=request.user,
            branch=branch,
            cgpa=cgpa,
            skills=skills,
            backlog=backlog
        )

        return redirect('dashboard')

    return render(request, 'profile.html')


def user_logout(request):
    logout(request)
    return redirect('home')
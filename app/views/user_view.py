from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def add_user(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('course_list')
    else:
        user_form = UserCreationForm(request.POST)
    return render(request, "user/user_form.html", {"user_form": user_form})


def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('course_list')
        else:
            messages.error(request, 'Credentials not valid')
            return redirect('user_login')
    else:
        form_login = AuthenticationForm()
    return render(request, "user/login.html", {"form_login": form_login})


def user_logout(request):
    logout(request)
    return redirect('user_login')

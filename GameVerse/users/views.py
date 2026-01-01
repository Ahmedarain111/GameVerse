from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from .forms import SignupForm, LoginForm

User = get_user_model()


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("main:home")
    else:
        form = SignupForm()

    return render(request, "users/signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            
            if user:
                login(request, user)
                return redirect("main:home")
            
    else:
        form = LoginForm()
    
    return render(request, "users/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("users:login")
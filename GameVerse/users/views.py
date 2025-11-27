from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout


User = get_user_model()


def signup_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("pasword")
        user = User.objects.create_user(email=email, password=password)

        login(request, user)
        return redirect("dashboard")

    return render(request, "users/signup.html")


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect("dashboard")

    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")
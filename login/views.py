from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def success_page(request):
    return render(request, "success.html")
    
def registration_view(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["retype_password"]:
            User.objects.create_user(request.POST["username"], request.POST["email"], request.POST["password"])
            return redirect("/login/")
        else:
            return redirect("/registration/")
    else:
        return render(request, "registration.html")
    
def login_view(request):
    if request.method == "POST":
        user = authenticate(username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            return redirect("success_page")
        else:
            return redirect("/login/")
    else:
        return render(request, "login.html", {"next": "success"})

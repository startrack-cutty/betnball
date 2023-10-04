from django.shortcuts import render, HttpResponse
from .models import Users


# Create your views here.
def user_login(request):
    context = {
        'myusers': ['Jeff', 'Tiko', 'Joose', 'Al']
    }
    return render(request, 'users/user-login.html', context)

def get_user(request, username, password):
    return HttpResponse(f"You entered username: {username} and password: {password}")

def get_friends(request):
    return HttpResponse("Get All Friends for this user...")

def get_all_users(request):
    context = {
        'appusers': Users.objects.all()
    }

    return render(request, "users/user-login.html", context)

from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello and Welcome to the Ball & Parlay Web Application")

def login(request):
    # Open page to allow user to enter login credentials
    pass

def create_account(request):
    # Open page to allow user to create user account
    pass
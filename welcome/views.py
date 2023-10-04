from django.shortcuts import render, HttpResponse

# Create your views here.
def show_options(request):
    return HttpResponse("Thanks for logging in...  What would you like to do?")
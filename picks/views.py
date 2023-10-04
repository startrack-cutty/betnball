from django.shortcuts import render, HttpResponse

# Create your views here.
def get_user_picks(request):
    return HttpResponse("Get all of the user's picks here...")
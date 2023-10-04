from django.shortcuts import render, HttpResponse

# Create your views here.
def get_user_pools(request):
    return HttpResponse("Get all of the user's pools...")
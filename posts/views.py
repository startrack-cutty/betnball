from django.shortcuts import render, HttpResponse

# Create your views here.
def get_posts(request):
    return HttpResponse("Get all Posts for the user...")
from django.shortcuts import render, HttpResponse

# Create your views here.
def open_main_page(request):
    return HttpResponse("Get all Pools...")
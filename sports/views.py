from django.shortcuts import render, HttpResponse

# Create your views here.
def get_all_sports(request):
    return HttpResponse("Get all Sports from the database...")
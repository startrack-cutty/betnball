from django.shortcuts import render, HttpResponse

# Create your views here.
def get_all_teams(request):
    return HttpResponse("Get all teams from the database...")
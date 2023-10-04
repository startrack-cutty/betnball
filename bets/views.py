from django.shortcuts import render, HttpResponse

# Create your views here.
def get_user_bets(request):
    return HttpResponse("Get User's bets...")
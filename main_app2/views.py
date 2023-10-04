from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Welcome to The Poolz")
    return render(request, "main_app2/_base.html", {})
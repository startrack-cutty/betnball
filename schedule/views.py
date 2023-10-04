from django.shortcuts import render, HttpResponse
from .models import Schedule

# Create your views here.
def get_schedule(request):
    context = {
        'games': Schedule.objects.all()
    }

    return render(request, "schedule/schedule.html", context)
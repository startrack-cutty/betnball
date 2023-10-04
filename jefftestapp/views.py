from django.shortcuts import render, HttpResponse
from .models import Test


# Create your views here.
def showUrls(request):
    # return HttpResponse("Loading JeffTestApp Page")
    favUrls = Test.objects.all()
    context = {
        'favUrls': favUrls
    }
    return render(request, 'jefftestapp/test.html', context)




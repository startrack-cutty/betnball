from django.shortcuts import render, HttpResponse

# Create your views here.
def get_billing_info(request):
    return HttpResponse("Get billing info here...")
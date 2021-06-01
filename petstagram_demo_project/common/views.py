from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def landing_page(request):
    return render(request, 'landing_page.html')


# def testing_view(request):
#     return HttpResponse("testing_view http response")

from django.shortcuts import render, HttpResponse
from datetime import datetime
from time import gmtime, strftime

# Create your views here.
def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M:%S", gmtime()),
    }
    return render(request, 'page.html', context)

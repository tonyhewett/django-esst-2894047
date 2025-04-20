from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    # return HttpResponse(' Hello world Apr 2025')
    return render(request, 'home/welcome.html', {'today': datetime.today()})

@login_required(login_url='/admin')
def authorised(request):
    return render(request, 'home/authorised.html', {'today': datetime.today()})

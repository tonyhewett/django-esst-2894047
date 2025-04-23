from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}

class AuthorisedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorised.html'
    login_url = '/admin'
    

''' replaced with class view HomeView above
def home(request):
    # return HttpResponse(' Hello world Apr 2025')
    return render(request, 'home/welcome.html', {'today': datetime.today()})
'''
'''
@login_required(login_url='/admin')
def authorised(request):
    return render(request, 'home/authorised.html', {'today': datetime.today()})
'''
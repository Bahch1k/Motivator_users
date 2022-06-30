
import re
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from .forms import UserCreationForm, MotivationForm
from django.contrib.auth import authenticate, login
from .models import Motivation, User
from django.conf import settings


class Register(CreateView):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
             'form': UserCreationForm() 
            }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

def list(request):
    motivations = Motivation.objects.all()
    return render(request, 'main.html', {'motivations': motivations})


class MotivationView(CreateView):
    template_name = 'post.html'

    def get(self, request):
        if request.user.is_authenticated:
            form = MotivationForm
            context = {
                'form': form
                
            }
            return render(request, self.template_name, context)
        else:
            return redirect(settings.LOGIN_URL)

    def post(self, request):
        form = MotivationForm(request.POST)
        
        if form.is_valid():
            motivation = form.save(commit=False)
            motivation.nickname = request.user
            motivation.save()
            return redirect('main')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

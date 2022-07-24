from django.http import Http404
from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView
from .forms import UserCreationForm, MotivationCreateForm
from django.contrib.auth import authenticate, login
import requests


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


class MotivationList(ListView):
    
    template_name = 'main.html'

    def get(self, request):
        response = requests.get('http://motivations:9000/motivations/')
        page_obj = response.json
        return render(request, self.template_name, {'page_obj':page_obj})

class DetailMotivationList(ListView):
    template_name = 'maintest.html'

    def get(self, request, id):
        url = 'http://motivations:9000/motivations/'
        response = requests.get(url + str(id))
        motivation = response.json()
        return render(request, self.template_name, {'motivation': motivation})


class RandomMotivation(ListView):

    template_name = 'home.html'

    def get(self, request):
        response = requests.get('http://motivations:9000/motivations/random')
        random_motivation = response.json()
        return render(request, self.template_name, {'random_motivation': random_motivation})


class MotivationCreate(CreateView):
    template_name = 'post.html'

    def get(self, request):
        form = MotivationCreateForm
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = MotivationCreateForm(request.POST)

        if form.is_valid():
            new_motivaion = form.cleaned_data.get('motivation')
            user = request.user.username
            response = requests.post('http://motivations:9000/motivations/new', json={
                'nickname': user,
                'motivation': new_motivaion
            })
            return redirect('main')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

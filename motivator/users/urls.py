
from django.urls import include, path
from .views import MotivationView, Register, list, random_motivation

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('motivations/create', MotivationView.as_view(), name='motivations'),
    path('motivations/', list, name='main'),
    path('', random_motivation, name='home')
]

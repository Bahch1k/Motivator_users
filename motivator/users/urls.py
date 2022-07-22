
from django.urls import include, path
from .views import Register, MotivationList, MotivationCreate

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('motivations/', MotivationList.as_view(), name='main'),
    path('motivations/new', MotivationCreate.as_view(), name='motivations')
]

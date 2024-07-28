from django.urls import  path
from . import views

urlpatterns = [
      
      path('register/', views.sign_up_by_django, name='register'),
      path('register2/', views.sign_up_by_html, name='register2'),
]
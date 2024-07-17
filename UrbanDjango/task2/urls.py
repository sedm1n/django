from django.urls import  path
from . import views

urlpatterns = [
      path('func', views.func_template, name='func_templ'),
      path('class', views.ClassTemplate.as_view(), name='class_templ'),
]
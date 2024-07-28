from re import U
from django.shortcuts import render

from .forms import UserRegister
# Create your views here.
USERS = {
      'ivan':'12345',
      'petr':'12345',
      }

def sign_up_by_django(request):
      context = {}
      info = {}
      if request.method == 'POST':
            form =  UserRegister(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  password = form.cleaned_data['password']
                  password2 = form.cleaned_data['repeat_password']
                  age = int(form.cleaned_data['age'])

                  context = {'username':username}

                  if username in USERS:
                        info['error'] = "Такой пользователь уже существует"
                  elif password != password2:
                        info['error'] = "Пароли не совпрадают"
                  elif age < 18:
                        info['error'] = "Вы должны быть старше 18"
                  else:
                        info['info'] = "Приветствуем тебя {}".format(username)

                  context = {"form":form.cleaned_data,
                             }
      else:
            form = UserRegister()
      
      context = {"info":info,}
      return render(request, 'fifth_task/registration_page.html', context)

def sign_up_by_html(request):
      info = {}
      context = {}

      if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            password2 = request.POST['repeat_password']
            age = int(request.POST['age'])

            if username in USERS:
                  info['error'] = "Такой пользователь {} уже существует".format(username)
            elif password != password2:
                  info['error'] = "Пароли не совпрадают"
            elif age < 18:
                  info['error'] = "Вы должны быть старше 18"
            else:
                  info['info'] = "Приветствуем тебя {}".format(username)
                  
      context = {'info':info}
      return render(request, 'fifth_task/registration_page.html', context)

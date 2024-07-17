from django.shortcuts import render

# Create your views here.
def index(request):

      return render(request, 'third_task/index.html')

def shop(request):
      goods = {
               'Atomic':'1400',
               'Cyberpunck':'2500',
               'PayDay':'1600'
               }
      return render(request, 'third_task/shop.html', {'goods':goods})

def cart(request):
      cart_goods = {'Atomic':'1 400'}
      return render(request, 'third_task/cart.html', {'cart_goods':cart_goods})
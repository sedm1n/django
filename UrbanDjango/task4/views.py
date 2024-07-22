from django.shortcuts import render

# Create your views here.
def index(request):
      pagename = "Главна страница"
      context = {'pagename': pagename}
      return render(request, 'fourth_task/index.html', context)

def shop(request):
      goods ={
                  'games': ["Atomic Heart", "Cyberpunk 2077"],
                    
                            }
      pagename = "Магазин"        
      context = {'goods':goods, 'pagename':pagename}

      return render(request, 'fourth_task/shop.html', context)

def cart(request):
      pagename = "Корзина"
      cart_goods = {'Atomic':'1 400'}
      return render(request, 'fourth_task/cart.html', {'cart_goods':cart_goods,
                                                       'pagename':pagename})
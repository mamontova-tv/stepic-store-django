from django.shortcuts import render, HttpResponseRedirect
from products.models import ProductCategory, Product, Basket
from users.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    # return HttpResponse('Hello there')
    # return render(request, "products/test.html", {'title': 'Test Template'})
    context = {
        'title': 'Test Title',
        'is_promotion': False
        }
    return render(request, 'products/index.html', context)

def products(request, category_id=0, page_num=1):
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    per_page = 2
    paginator = Paginator(object_list=products, per_page=per_page)
    products_paginator = paginator.page(page_num)

    context = {
        'title': 'Store - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': products_paginator,
        'selected_cat': category_id,
        }
    return render(request, 'products/products.html', context)


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META["HTTP_REFERER"])

@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()

    return HttpResponseRedirect(request.META["HTTP_REFERER"])

    # [
    #                     {
    #                     'image': '/static/vendor/img/products/Adidas-hoodie.png',
    #                     'name': 'Худи черного цвета с монограммами adidas Originals',
    #                     'price': 6090,
    #                     'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни'
    #                     },
    #                     {
    #                     'image': '/static/vendor/img/products/Blue-jacket-The-North-Face.png',
    #                     'name': 'Синяя куртка The North Face',
    #                     'price': 23725,
    #                     'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'
    #                     },
    #                     {
    #                     'image': '/static/vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
    #                     'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
    #                     'price': 3390,
    #                     'description': 'Материал с плюшевой текстурой. Удобный и мягкий'
    #                     },
    #                     {
    #                     'image': '/static/vendor/img/products/Black-Nike-Heritage-backpack.png',
    #                     'name': 'Черный рюкзак Nike Heritage',
    #                     'price': 2340,
    #                     'description': 'Плотная ткань. Легкий материал.'
    #                     },
    #                     {
    #                     'image': '/static/vendor/img/products/Black-Dr-Martens-shoes.png',
    #                     'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
    #                     'price': 13590,
    #                     'description': 'Гладкий кожаный верх. Натуральный материал.'
    #                     },
    #                     {
    #                     'image': '/static/vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
    #                     'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
    #                     'price': 2890,
    #                     'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.'
    #                     }
    #                 ]
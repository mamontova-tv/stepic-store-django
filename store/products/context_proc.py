from products.models import Basket


def category_id(request):
    from products.views import products
    return {'category_id': products.category_id}


def baskets(request):
    user = request.user
    return {'baskets': Basket.objects.filter(user=user) if user.is_authenticated else []}

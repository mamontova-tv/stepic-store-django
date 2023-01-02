

def category_id(request):
    from products.views import products
    return {'category_id': products.category_id}
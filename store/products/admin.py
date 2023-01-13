from django.contrib import admin

from products.models import Product, ProductCategory

# Register your models here.


admin.site.register(ProductCategory)
admin.site.register(Product)


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name', 'price', 'quantity', 'category']
#     fields = ['name', 'description', ['price', 'quantity'], 'image', 'category']
#     readonly_fields = ['description']
#     search_fields = ['name']
#     ordering = ['name']

# class BasketAdmin(admin.TabularInline):
#     model = Basket
#     fields = ['product', 'category']
#     extra = 0

from django.contrib import admin
from .models import Product
from django.contrib.auth.models import Group

admin.site.site_header = 'DateMaster Dashboard'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('lot', 'name', 'category', 'expiration_date', 'observation')
    list_filter = ('category', 'expiration_date')

# Register your models here.
admin.site.register(Product, ProductAdmin)
# admin.site.unregister(Group)

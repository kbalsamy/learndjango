from django.contrib import admin
from .models import Catagory, Product


# Register your models here.
@admin.register(Catagory)
class CatagoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug']
    ordering = ['name']
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class CatagoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'price', 'available']
    ordering = ['name']
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('available',)

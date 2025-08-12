from django.contrib import admin
from .models import Car, Brand, CarInventory


# @admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['model', 'brand', 'factory_year', 'model_year', 'value']
    search_fields = ['model', 'model_year']
    list_filter = ['factory_year']


class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)

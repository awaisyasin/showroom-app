from django.contrib import admin
from .models import *

# Register your models here.
class ShowRoomAdmin(admin.ModelAdmin):
    def get_brands(self, obj):
        brands =  ", ".join([str(brand) for brand in obj.brands.all()])
        return brands
    get_brands.short_description = 'Brands'

    list_display = ('name', 'get_brands',  'city', 'state', 'country')
    list_filter = ('city', 'state', 'country')

class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'showroom', 'age', 'gender', 'email')
    list_filter = ('gender',)

class BrandAdmin(admin.ModelAdmin):
    def get_showrooms(self, obj):
        showrooms  =  ",".join([str(showroom) for showroom in obj.showroom.all()])
        return showrooms
    get_showrooms.short_description = 'ShowRooms'
    list_display = ('name', 'get_showrooms')

class ModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'year', 'price')
    list_filter = ('brand',)

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'chasis_number')

class EngineAdmin(admin.ModelAdmin):
    list_display = ('engine_number', 'car', 'type', 'horsepower', 'torque')

class FeaturesAdmin(admin.ModelAdmin):
    list_display = ('feature',)

admin.site.register(ShowRoom, ShowRoomAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Model, ModelAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Engine, EngineAdmin)
admin.site.register(Features, FeaturesAdmin)


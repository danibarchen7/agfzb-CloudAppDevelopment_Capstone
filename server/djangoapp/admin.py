from django.contrib import admin
from .models import CarMake, CarModel
# from .models import related models


# Register your models here.
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 2
# CarModelInline class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'year')
    list_filter = ['year']
    search_fields = ['name', 'type']
# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('name', 'description')


# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)

from django.contrib import admin
from rentcar.models import Car


# Register your models here.
@admin.register(Car)
class AdminCar(admin.ModelAdmin):
    list_display = ('id', 'make', 'model', 'year', )
    list_display_links = ('id', 'make', )
    list_per_page = 50
    list_filter = ('year', )

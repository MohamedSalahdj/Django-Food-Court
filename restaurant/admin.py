from django.contrib import admin
from .models import Restaurant, Category, Dish, Review

admin.site.register(Restaurant)
admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Review)

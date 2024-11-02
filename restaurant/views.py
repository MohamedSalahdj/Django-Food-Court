from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Restaurant, Category, Dish


class ListRestaurants(ListView):
    model = Restaurant    


class DetailRestaurants(ListView):
    model = Dish
    template_name = 'restaurant/resturant_detail.html'
    
    def get_queryset(self):
        restaurant = Restaurant.objects.get(slug=self.kwargs['slug'])
        queryset = super().get_queryset().filter(restaurant=restaurant)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        restaurant = get_object_or_404(Restaurant, slug=self.kwargs['slug'])
        categories = restaurant.categories.all()
        context['restaurant'] = restaurant
        context['categories'] = categories
        return context
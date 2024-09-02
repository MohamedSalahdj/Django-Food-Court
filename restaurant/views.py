from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView


from .models import Restaurant, Category, Dish


class ListRestaurant(ListView):
    model = Restaurant
    
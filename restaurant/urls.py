from django.urls import path
from .views import ListRestaurants, DetailRestaurants

app_name = 'restaurant.apps.RestaurantConfig'

urlpatterns = [
    path('restaurnts/', ListRestaurants.as_view(), name='list_restaurant'),
    path('restaurnts/<slug:slug>', DetailRestaurants.as_view(), name='detail_restaurant'),

]

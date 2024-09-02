from django.urls import path
from .views import ListRestaurant

app_name = 'restaurant.apps.RestaurantConfig'

urlpatterns = [
    path('restaurnts/', ListRestaurant.as_view(), name='list_restaurant'),
]

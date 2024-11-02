from django.urls import path
from .views import ListRestaurants, DetailRestaurants, dish_details

app_name = 'restaurant.apps.RestaurantConfig'

urlpatterns = [
    path('restaurnts/', ListRestaurants.as_view(), name='list_restaurant'),
    path('restaurnts/<slug:slug>/', DetailRestaurants.as_view(), name='detail_restaurant'),
    path('restaurnt/<slug:restaurant_slug>/<slug:slug>/', dish_details, name='dish_details'),

]

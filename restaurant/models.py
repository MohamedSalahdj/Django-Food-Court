from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

restaurant_status = (
    ("Open", "Open"),
    ("Closed", "Closed")
)

class Restaurant(models.Model):
    restaurant_id = models.AutoField(_("Restaurant ID"), primary_key=True)
    name = models.CharField(_("Name"), max_length=100)
    description = models.TextField(_("Description"), max_length=350)
    status = models.CharField(_("Status"), max_length=6, choices=restaurant_status, default="Open")
    slug = models.SlugField(_("Slug"), blank=True)
    categories = models.ManyToManyField('Category', verbose_name=_("Category"), related_name='restaurant_categories')
    image = models.ImageField(_("Restaurant Image"), upload_to="Restaurants")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Restaurant, self).save(*args, **kwargs)


class Category(models.Model):
    category_id = models.AutoField(_("Category ID"), primary_key=True)
    name = models.CharField(_("Name"), max_length=150)
    slug = models.SlugField(_("Slug"), blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Dish(models.Model):
    dish_id = models.BigAutoField(_("Dish ID"), primary_key=True)
    name = models.CharField(_("Name"), max_length=150)
    description = models.TextField(_("Description"), max_length=750)
    price =models.DecimalField(_("Price"), max_digits=10, decimal_places=2)
    image = models.ImageField(_("Dish Image"), upload_to="Dish")
    created_at = models.DateTimeField(_("Created at"), default=timezone.now)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    restaurant = models.ForeignKey(Restaurant, verbose_name=_("Restaurant"), on_delete=models.CASCADE, related_name="dish_restaurant")
    category = models.ForeignKey(Category, verbose_name=_("Category"), on_delete=models.CASCADE, related_name="dish_category")
    slug = models.SlugField(_("Slug"), blank=True)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Dish, self).save(*args, **kwargs)


class Review(models.Model):
    review = models.TextField(_("Review"), max_length=350)
    rate = models.PositiveSmallIntegerField(_("Rate"),
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.CASCADE, related_name="user_reviews")
    dish = models.ForeignKey(Dish, verbose_name=_("Dish"), on_delete=models.CASCADE, related_name="dish_reviews")
    created_at = models.DateTimeField(_("Created at"), default=timezone.now)

    def __str__(self):
        return f"{self.user} - {self.rate} - {self.review}"



from django.db import models
from django.utils.text import slugify

restaurant_status = (
    ("Open", "Open"),
    ("Closed", "Closed")
)

class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=350)
    status = models.CharField(max_length=6, choices=restaurant_status, default="Open")
    slug = models.SlugField(blank=True)
    categories = models.ManyToManyField('Category', related_name='restaurant_categories')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Restaurant, self).save(*args, **kwargs)


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)



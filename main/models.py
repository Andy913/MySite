from django.db import models
from datetime import datetime

# Create your models here.
class PageCategory(models.Model):
    page_category = models.CharField(max_length=200)
    category_blurb = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Page Categories"

    def __str__(self):
        return self.page_category


# class LifestyleCategory(models.Model):
#     lifestyle_category = models.CharField(max_length=200)
#     category_summary = models.CharField(max_length=200)

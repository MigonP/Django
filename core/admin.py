from django.contrib import admin
from .models import Film, Category, Rate

admin.site.register(Film)
admin.site.register(Category)
admin.site.register(Rate)
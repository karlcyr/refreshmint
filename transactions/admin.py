from django.contrib import admin

# Register your models here.
from .models import Transaction, Category

admin.site.register(Category)
admin.site.register(Transaction)


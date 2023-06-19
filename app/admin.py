from django.contrib import admin

# Register your models here.
from app.models import *

admin.site.register(product_category)

admin.site.register(product)
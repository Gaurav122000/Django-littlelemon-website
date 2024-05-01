from django.contrib import admin
from .models import Menu
from .models import Booking
# This allows the Menu model to be managed through the Django admin interface.
# Register your models here.
admin.site.register(Menu)

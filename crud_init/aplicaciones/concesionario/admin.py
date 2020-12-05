from django.contrib import admin
from .models import User, Car

# Here I have to import my models to add to /admin
admin.site.register(User)
admin.site.register(Car)


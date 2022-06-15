from django.contrib import admin
from .models import Templates
from .models import User

# Register your models here.

admin.site.register(Templates)
admin.site.register(User)
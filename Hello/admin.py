from django.contrib import admin

# Register your models here.
from .models import students

admin.site.register(students)

from .models import Information  # import your model

admin.site.register(Information) # actual registration




from django.contrib import admin
from .models import Vacancy, Category
from .models import Company


admin.site.register(Vacancy)
admin.site.register(Category)
admin.site.register(Company)

# Register your models here.

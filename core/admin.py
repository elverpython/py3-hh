from django.contrib import admin
from .models import Vacancy, Category, Skill
from .models import Company


admin.site.register(Vacancy)
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Skill)

# Register your models here.

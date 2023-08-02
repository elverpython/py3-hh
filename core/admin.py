from django.contrib import admin
from .models import Vacancy, Category, Skill
from .models import Company


#admin.site.register(Vacancy)
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Skill)

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['title', 'salary', 'is_relevant', 'contacts']

# Register your models here.

from django.contrib import admin
from .models import Company, Vacancy, Application, Specialty


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    pass


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    pass


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    pass

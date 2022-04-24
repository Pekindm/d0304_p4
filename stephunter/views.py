from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, ListView
from stephunter.models import Specialty, Company, Vacancy
from django.db.models import Count
from django.http import Http404


class MainView(View):
    def get(self, request):
        specialties = Specialty.objects.annotate(count_vacancies=Count('vacancies'))
        companies = Company.objects.annotate(count_vacancies=Count('vacancies'))
        return render(request, 'stephunter/index.html', context={
            "specialties": specialties,
            "companies": companies,
        })


class VacanciesView(View):
    def get(self, request):
        title = "Все вакансии"
        vacancies = Vacancy.objects.all()
        return render(request, 'stephunter/vacancies.html', context={
            "title": title,
            "vacancies": vacancies,
        })


class VacanciesSpecView(View):
    def get(self, request, vac_spec):
        try:
            title = Specialty.objects.get(code=vac_spec).title
            vacancies = Vacancy.objects.filter(specialty=Specialty.objects.get(code=vac_spec).id)
        except KeyError:
            raise Http404
        return render(request, 'stephunter/vacancies.html', context={
            "title": title,
            "vacancies": vacancies,
        })


class CompanyView(View):
    def get(self, request, id):
        try:
            company = Company.objects.annotate(count_vacancies=Count('vacancies')).get(id=id)
            vacancies = Vacancy.objects.filter(company=id)
        except KeyError:
            raise Http404
        return render(request, 'stephunter/company.html', context={
            "company": company,
            "vacancies": vacancies,
        })


class VacancyView(View):
    def get(self, request, id):
        try:
            vacancy = Vacancy.objects.get(id=id)
        except KeyError:
            raise Http404
        return render(request, 'stephunter/vacancy.html', context={
            "vacancy": vacancy,
        })

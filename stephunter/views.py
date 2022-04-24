from django.conf import settings
from django.shortcuts import render
from django.views import View
from stephunter.models import Specialty, Company, Vacancy
from django.db.models import Count
from django.http import Http404


def main_view(request):
    try:
        context = {
            "specialties": Specialty.objects.annotate(count_vacancies=Count('vacancies')),
            "companies": Company.objects.annotate(count_vacancies=Count('vacancies')),
            "vacancies": Vacancy.objects.all(),
        }
    except KeyError:
        raise Http404
    return render(request, 'stephunter/index.html', context=context)


def vacancies_view(request):
    try:
        context = {
            "spec": "Все вакансии",
            "vacancies": Vacancy.objects.all(),
            "companies": Company.objects.annotate(count_vacancies=Count('vacancies')),
        }
    except KeyError:
        raise Http404
    return render(request, 'stephunter/vacancies.html', context=context)


def specialization_view(request, vac_spec):
    try:
        context = {
            "spec": Specialty.objects.get(code=vac_spec).title,
            "vacancies": Vacancy.objects.filter(specialty=Specialty.objects.get(code=vac_spec).id),
        }
    except KeyError:
        raise Http404
    return render(request, 'stephunter/vacancies.html', context=context)


def company_view(request, id):
    try:
        context = {
            "company": Company.objects.annotate(count_vacancies=Count('vacancies')).get(id=id),
            "vacancies": Vacancy.objects.filter(company=id),
        }
    except KeyError:
        raise Http404
    return render(request, 'stephunter/company.html', context=context)


def vacancy_view(request, id):
    try:
        context = {
            "vacancy": Vacancy.objects.get(id=id),
        }
    except KeyError:
        raise Http404
    return render(request, 'stephunter/vacancy.html', context=context)

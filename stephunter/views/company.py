from django.shortcuts import render
from django.views.generic import View
from stephunter.models import Company, Vacancy
from django.db.models import Count
from django.http import Http404


class CompanyView(View):
    def get(self, request, id):
        try:
            company = Company.objects.annotate(count_vacancies=Count('vacancies')).get(id=id)
            vacancies = Vacancy.objects.filter(company=id)
        except KeyError:
            raise Http404
        return render(request, 'stephunter/company/company.html', context={
            "company": company,
            "vacancies": vacancies,
        })

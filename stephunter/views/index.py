from django.shortcuts import render
from django.views.generic import View, ListView
from stephunter.models import Specialty, Company, Vacancy
from django.db.models import Count, Q


class MainView(View):
    def get(self, request):
        specialties = Specialty.objects.annotate(count_vacancies=Count('vacancies'))
        companies = Company.objects.annotate(count_vacancies=Count('vacancies'))
        return render(request, 'stephunter/main/index.html', context={
            "specialties": specialties,
            "companies": companies,
        })


class SearchView(ListView):
    model = Vacancy
    template_name = "stephunter/main/search.html"

    def get_queryset(self):
        request = self.request.GET.get('srch')
        return Vacancy.objects.filter(
            Q(title__icontains=request) | Q(description__icontains=request) | Q(skills__icontains=request),
        )

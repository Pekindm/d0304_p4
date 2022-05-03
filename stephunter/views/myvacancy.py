from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import View
from stephunter.models import Company, Vacancy, Application
from django.db.models import Count
from stephunter.forms import VacancyForm
from django.utils import timezone


class MyVacanciesView(View):
    def get(self, request):
        vacancies = Vacancy.objects.filter(company__owner_id=request.user.id).annotate(
            application_count=Count('applications'))
        return render(request, 'stephunter/vacancy/vacancy-list.html', context={
            'vacancies': vacancies,
        })


class MyVacancyView(LoginRequiredMixin, View):
    def get(self, request, vacancy_id):
        vacancy = Vacancy.objects.filter(id=vacancy_id, company__owner_id=request.user.id) \
            .annotate(application_count=Count('applications')).first()
        if vacancy:
            applications = Application.objects.filter(vacancy_id=vacancy_id)
            form = VacancyForm(instance=vacancy)
            return render(request, 'stephunter/vacancy/vacancy-edit.html', context={
                'applications': applications,
                'vacancy': vacancy,
                'form': form,
            })
        return redirect('my_vacancies')

    def post(self, request, vacancy_id):
        form = VacancyForm(request.POST)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.id = vacancy_id
            vacancy.company = Company.objects.get(owner=self.request.user)
            vacancy.published_at = timezone.now()
            vacancy.save()
            messages.add_message(request, messages.SUCCESS, 'Вакансия обновлена!')
            return redirect('my_vacancies')
        messages.add_message(request, messages.ERROR, 'Ошибка!')
        return render(request, 'stephunter/vacancy/vacancy-edit.html', context={
            'form': form,
        })


class MyVacancyCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = VacancyForm()
        return render(request, 'stephunter/vacancy/vacancy-edit.html', context={
            'form': form,
        })

    def post(self, request):
        form = VacancyForm(request.POST)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.company = Company.objects.get(owner=self.request.user)
            vacancy.published_at = timezone.now()
            vacancy.save()
            messages.add_message(request, messages.SUCCESS, 'Вакансия обновлена!')
            return redirect('my_vacancies')
        messages.add_message(request, messages.ERROR, 'Ошибка!')
        return render(request, 'stephunter/vacancy/vacancy-edit.html', context={
            'form': form,
        })

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from stephunter.models import Specialty, Vacancy, Application
from django.http import Http404
from django.contrib.auth.models import User
from stephunter.forms import SendApplicationForm


class VacanciesView(View):
    def get(self, request):
        title = "Все вакансии"
        vacancies = Vacancy.objects.all()
        return render(request, 'stephunter/vacancy/vacancies.html', context={
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
        return render(request, 'stephunter/vacancy/vacancies.html', context={
            "title": title,
            "vacancies": vacancies,
        })


# просмотр вакансии
class VacancyView(View):
    def get(self, request, id):
        vacancy = get_object_or_404(Vacancy, id=id)
        return render(request, 'stephunter/vacancy/vacancy.html', context={
            "vacancy": vacancy,
            'form': SendApplicationForm,
        })

    def post(self, request, id):
        vacancy = get_object_or_404(Vacancy, id=id)
        form = SendApplicationForm(request.POST)
        if form.is_valid():
            written_username = form.cleaned_data.get('written_username')
            written_phone = form.cleaned_data.get('written_phone')
            written_cover_letter = form.cleaned_data.get('written_cover_letter')
            if request.user.id:
                Application.objects.create(
                    written_username=written_username,
                    written_phone=written_phone,
                    written_cover_letter=written_cover_letter,
                    user=User.objects.get(id=request.user.id),
                    vacancy=Vacancy.objects.get(id=id),
                )
            else:
                return redirect('login')
            return redirect('send', id)
        return render(request, 'stephunter/vacancies/vacancy.html', context={
            'vacancy': vacancy,
            'form': form,
        })


# отправка вакансии
class SendView(View):
    def get(self, request, vacancy_id):
        return render(request, 'stephunter/vacancy/sent.html', context={
            "vacancy_id": vacancy_id,
        })

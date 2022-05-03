"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from accounts.views import RegisterView, MyLoginView
from stephunter.views.index import MainView, SearchView
from stephunter.views.company import CompanyView
from stephunter.views.vacancies import VacanciesView, VacanciesSpecView, VacancyView, SendView
from stephunter.views.mycompany import MyCompanyStartView, MyCompanyCreateView, MyCompanyView
from stephunter.views.myvacancy import MyVacanciesView, MyVacancyView, MyVacancyCreateView
from stephunter.views.resume import ResumeNewView, ResumeView, ResumeCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='index'),
    path('search/', SearchView.as_view(), name='search'),

    path('companies/<int:id>/', CompanyView.as_view(), name='company'),

    path('vacancies/', VacanciesView.as_view(), name='vacancies'),
    path('vacancies/cat/<str:vac_spec>/', VacanciesSpecView.as_view(), name='vac_spec'),
    path('vacancies/<int:id>/', VacancyView.as_view(), name='vacancy'),
    path('vacancies/<int:vacancy_id>/send/', SendView.as_view(), name='send'),

    path('mycompany/letsstart/', MyCompanyStartView.as_view(), name='lets_start'),
    path('mycompany/create/', MyCompanyCreateView.as_view(), name='my_company_create'),
    path('mycompany/', MyCompanyView.as_view(), name='my_company'),

    path('mycompany/vacancies/', MyVacanciesView.as_view(), name='my_vacancies'),
    path('mycompany/vacancies/<int:vacancy_id>', MyVacancyView.as_view(), name='my_vacancy'),
    path('mycompany/vacancies/new', MyVacancyCreateView.as_view(), name='my_vac_create'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('resume/new', ResumeNewView.as_view(), name='resume_new'),
    path('resume/create', ResumeCreateView.as_view(), name='resume_create'),
    path('resume/', ResumeView.as_view(), name='resume'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT,
                          )
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls'))]

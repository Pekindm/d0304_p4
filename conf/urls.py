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
from django.urls import path

from stephunter.views import main_view
from stephunter.views import vacancies_view
from stephunter.views import specialization_view
from stephunter.views import company_view
from stephunter.views import vacancy_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='index'),
    path('vacancies/', vacancies_view, name='vacancies'),
    path('vacancies/cat/<str:vac_spec>/', specialization_view, name='vac_spec'),
    path('companies/<int:id>/', company_view, name='company'),
    path('vacancies/<int:id>/', vacancy_view, name='vacancy'),
]

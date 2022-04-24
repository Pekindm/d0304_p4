from django.core.management.base import BaseCommand
from stephunter.models import Specialty, Vacancy, Company
import stephunter.data as data


class Command(BaseCommand):

    def handle(self, *args, **options):
        """ Категории """
        for specialty in data.specialties:
            if Specialty.objects.filter(code=specialty["code"]).count() == 0:
                new_specialty = Specialty(code=specialty["code"],
                                          title=specialty["title"],
                                          picture="https://place-hold.it/100x60"
                                          )
                new_specialty.save()

        """ Компании """
        for company in data.companies:
            new_company = Company(id=company["id"],
                                  name=company["title"],
                                  location=company["location"],
                                  logo="https://place-hold.it/100x60",
                                  description=company["description"],
                                  employee_count=int(company["employee_count"])
                                  )
            new_company.save()

        """ Вакансии """
        for job in data.jobs:
            new_job = Vacancy(id=job["id"],
                              title=job["title"],
                              skills=job["skills"],
                              description=job["description"],
                              specialty=Specialty.objects.get(code=job["specialty"]),
                              company=Company.objects.get(id=job["company"]),
                              salary_min=int(job["salary_from"]),
                              salary_max=int(job["salary_to"]),
                              published_at=job["posted"],
                              )
            new_job.save()

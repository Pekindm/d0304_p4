from django.db import models


class Specialty(models.Model):
    code = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    picture = models.URLField(default='https://place-hold.it/100x60')


"""
– Код (code) например, testing, gamedev
– Название (title)
– Картинка (picture) (URLField(default='https://place-hold.it/100x60'))
"""


class Company(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.TextField()
    employee_count = models.IntegerField()


"""
– Название (name)
– Город (location)
– Логотипчик (logo) (URLField(default='https://place-hold.it/100x60'))
– Информация о компании (description)
– Количество сотрудников (employee_count)
"""


class Vacancy(models.Model):
    title = models.CharField(max_length=120)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.CharField(max_length=120)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()


"""
– Название вакансии (title)
– Специализация (specialty) – связь с Specialty, укажите related_name="vacancies"
– Компания (company) – связь с Company, укажите related_name="vacancies"
– Навыки (skills)
– Текст (description)
– Зарплата от (salary_min)
– Зарплата до (salary_max)
– Опубликовано (published_at)
"""

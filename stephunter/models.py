from django.db import models
from django.contrib.auth.models import User
from conf.settings import MEDIA_COMPANY_IMAGE_DIR, MEDIA_SPECIALITY_IMAGE_DIR
from django.utils.translation import gettext_lazy as _


class Specialty(models.Model):
    code = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    picture = models.ImageField(upload_to=MEDIA_SPECIALITY_IMAGE_DIR)

    def __str__(self):
        return self.title


"""
– Код (code) например, testing, gamedev
– Название (title)
– Картинка (picture) (URLField(default='https://place-hold.it/100x60'))
"""


class Company(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    logo = models.ImageField(upload_to=MEDIA_COMPANY_IMAGE_DIR)
    description = models.TextField()
    employee_count = models.IntegerField()
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user', blank=True, null=True)

    def __str__(self):
        return self.name


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


class Application(models.Model):
    written_username = models.CharField(max_length=120)
    written_phone = models.CharField(max_length=15)
    written_cover_letter = models.TextField()
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='applications')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications', null=True)


class Resume(models.Model):
    class Status(models.TextChoices):
        NOT_IN_SEARCH = 'NIS', _('Не ищу работу')
        OPEN_TO_OFFERS = 'OTO', _('Открыт к предложениям')
        READY = 'RD', _('Ищу работу')

    class Qualification(models.TextChoices):
        JUNIOR = 'JUN', _('Junior')
        MIDDLE = 'MID', _('Middle')
        SENIOR = 'SNR', _('Senior')

    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='resume_owner', null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    status = models.CharField(max_length=3, choices=Status.choices)
    salary = models.IntegerField()
    qualification = models.CharField(max_length=3, choices=Qualification.choices)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='resume_spec')
    education = models.TextField()
    experience = models.TextField()
    portfolio = models.CharField(max_length=200)

    def __str__(self):
        return f'{ self.pk } { self.first_name } {self.status}'

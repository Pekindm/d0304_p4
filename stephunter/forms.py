from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from crispy_forms.layout import Field, Layout, Column, Row, HTML

from stephunter.models import Application, Company, Vacancy, Resume


class CustomCheckbox(Field):
    template = 'stephunter/company/custom_checkbox.html'


class SendApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['written_username', 'written_phone', 'written_cover_letter']
        labels = {
            'written_username': 'Ваше имя',
            'written_phone': 'Ваш телефон',
            'written_cover_letter': 'Сопроводительное письмо',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Откликнуться', css_class='btn btn-primary btn-lg btn-block'))
        self.helper.form_method = 'post'


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'location', 'logo', 'description', 'employee_count', 'owner')
        labels = {
            'name': 'Название компании',
            'location': 'География',
            'logo': 'Логотип',
            'description': 'Информация о компании',
            'employee_count': 'Количество сотрудников',
            'owner': 'Владелец компании',
        }
        widgets = {
            'logo': forms.FileInput(attrs={'class': '', 'multiple data-min-file-count': '0'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group pb-2 col-md-6 mb-0'),
                Column(
                    Row(
                        Column(HTML('<img src="/media/{{ form.logo.value }}" width="150" height="80">')),
                        Column('logo', css_class='form-group pb-2 col-md-6 mb-0'),
                        css_class='form-row',
                    )
                ),
                css_class='form-row',
            ),
            Row(
                Column('employee_count', css_class='form-group pb-2 col-md-6 mb-0'),
                Column('location', css_class='form-group pb-2 col-md-6 mb-0'),
                css_class='form-row',
            ),
            Row(
                Column('description', css_class='form-group'),
            ),
        )

        self.helper.add_input(Submit('submit', 'Сохранить'))


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ('title', 'specialty', 'skills', 'description', 'salary_min', 'salary_max')
        labels = {
            'title': 'Название вакансии',
            'specialty': 'Специальность',
            'skills': 'Требуемые навыки',
            'description': 'Описание вакансии',
            'salary_min': 'Зарплата от',
            'salary_max': 'Зарплата до',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Сохранить'))
        self.helper.form_method = 'post'


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('first_name', 'last_name', 'status', 'salary', 'specialty', 'qualification',
                  'education', 'experience', 'portfolio')
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'status': 'Готовность к работе',
            'salary': 'Ожидаемое вознаграждение',
            'specialty': 'Специализация',
            'qualification': 'Квалификация',
            'education': 'Образование',
            'experience': 'Опыт работы',
            'portfolio': 'Ссылка на портфолио',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Сохранить'))

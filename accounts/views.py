from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from accounts.forms import RegistrationForm, LoginForm


class RegisterView(CreateView):
    success_url = '/login'
    form_class = RegistrationForm
    template_name = 'accounts/register.html'


class MyLoginView(LoginView):
    form_class = LoginForm
    redirect_authenticated_user = True
    template_name = 'accounts/login.html'

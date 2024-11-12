
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserRegisterForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'


class UserLoginView(LoginView):
    form_class = AuthenticationForm
    success_url = reverse_lazy()

from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import BootstrapAuthenticationForm
from . import views


app_name = 'core'

urlpatterns = [
  path('', views.home, name='home'),
  path('dashboard/', views.dashboard, name='dashboard'),
  path('login/', auth_views.LoginView.as_view(
    template_name='auth/login.html',
    authentication_form=BootstrapAuthenticationForm
  ), name='login'),
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
  path('signup/', views.signup_view, name='signup'),
]

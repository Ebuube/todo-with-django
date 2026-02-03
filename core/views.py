from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect, render

from .forms import BootstrapUserCreationForm


def home(request):
    return render(request, 'core/home.html')

@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')


@require_http_methods(["GET", "POST"])
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('todos:list')

    form = BootstrapUserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('todos:list')

    return render(request, 'auth/signup.html', {'form': form})

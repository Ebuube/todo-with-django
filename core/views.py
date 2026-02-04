import logging
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect, render

from .forms import BootstrapUserCreationForm

logger = logging.getLogger(__name__)

def bad_request(request, exception=None):
    logger.warning('400 bad request', exc_info=exception)
    return render(request, 'errors/400.html', status=400)

def permission_denied(request, exception=None):
    logger.warning('403 permission denied', exc_info=exception)
    return render(request, 'errors/403.html', status=403)

def not_found(request, exception=None):
    logger.warning('404 not found', exc_info=exception)
    return render(request, 'errors/404.html', status=404)

def server_error(request):
    logger.error('500 server error', exc_info=True)
    return render(request, 'errors/500.html', status=500)

def home(request):
    return render(request, 'core/home.html')

@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')


@require_http_methods(["GET", "POST"])
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('todos:dashboard')

    form = BootstrapUserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('todos:dashboard')

    return render(request, 'auth/signup.html', {'form': form})

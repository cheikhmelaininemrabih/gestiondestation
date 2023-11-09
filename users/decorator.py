from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from django.http import HttpResponse
from functools import wraps

def active_and_role_required(role):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return HttpResponse("You need to be logged in.", status=401)
            if not request.user.profile.is_active:
                return HttpResponse("Your account is not activated.", status=403)
            if getattr(request.user.profile, f'is_{role}', False):
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You do not have the required role.", status=403)
        return _wrapped_view
    return decorator

def admin_required(function=None, redirect_field_name='next', login_url='user_login'):
    """
    Decorator for views that checks that the logged in user is a superuser (admin),
    redirecting to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

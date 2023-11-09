from django.http import HttpResponse
from functools import wraps

def active_and_role_required(role):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not hasattr(request.user, 'profile') or not request.user.profile.is_active:
                return HttpResponse("Your account is not activated.", status=403)
            if getattr(request.user.profile, f'is_{role}'):
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You do not have the required role.", status=403)
        return _wrapped_view
    return decorator

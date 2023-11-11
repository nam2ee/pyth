from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from profileapp.models import Profile


def decorator(func):
    def decorated(request, *args, **kwargs):
        if (Profile.objects.get(pk=kwargs['pk'])).user == request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return decorated
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def decorator(func):
    def decorated(request, *args, **kwargs):
        if User.objects.get(pk=kwargs['pk']) == request.user:
            #객체까지 가져온 것이 아니므로~!
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    return decorated

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorate import decorator
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile

# Create your views here.

deco_list = [
    login_required(login_url=reverse_lazy('accountapp:login')),
    decorator,
]


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    template_name = 'profileapp/create.html'
    success_url = reverse_lazy('accountapp:hello_world')
    context_object_name = 'target_profile'

    def form_valid(self, form):
        temp_profile = form.save(commit=False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})

@method_decorator(deco_list, 'get')
@method_decorator(deco_list, 'post')
class ProfileUpdateView(UpdateView):  # pk 처리하는 로직이 있어서 항상 올바른 pk를 줘야한다.
    model = Profile
    form_class = ProfileCreationForm
    context_object_name = 'target_profile'
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})

# 할 일: 데코레이터

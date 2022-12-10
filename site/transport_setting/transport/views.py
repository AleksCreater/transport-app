from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.template import loader
from django.shortcuts import render
from .models import Rubric
from django.views.generic.edit import CreateView
from .forms import UserForm
from django.urls import reverse_lazy


def index(request):
    bbs = User.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs':bbs, 'rubrics':rubrics,}
    return render(request, 'transport/index.html', context)


def by_rubric(request, rubric_id):
    bbs = User.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs':bbs, 'rubrics':rubrics,
               'current_rubric':current_rubric}
    return render(request, 'transport/by_rubric.html', context)

class UserCreateView(CreateView):
    template_name = 'transport/create.html'
    form_class = UserForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

"""class UserDeleteView(DeleteView):
    model = User
    success_url = '/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
"""

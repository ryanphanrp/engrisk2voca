from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Vocabulary
import random


# Create your views here.
class HomePage(LoginRequiredMixin, View):
    login_url = '/admin/login/'

    def get(self, request):
        vocabularys = list(Vocabulary.objects.all())
        random.shuffle(vocabularys)
        return render(request, 'home.html', {'vocabularys' : vocabularys})

@login_required(login_url="/admin/login/")
def quiz(request):
    vocabularys = list(Vocabulary.objects.all())
    random.shuffle(vocabularys)
    quizlist = list(vocabularys[:10])
    return render(request, 'quiz.html', {'vocabularys' : quizlist})

from django.shortcuts import render
from django.views import View
from .models import Vocabulary
import random


# Create your views here.
class HomePage(View):

    def get(self, request):
        vocabularys = list(Vocabulary.objects.all())
        random.shuffle(vocabularys)
        return render(request, 'home.html', {'vocabularys' : vocabularys})

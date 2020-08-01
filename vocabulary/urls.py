from django.urls import path
from .views import HomePage, quiz


app_name = 'vocabulary'

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('quiz', quiz, name='quiz'),
]
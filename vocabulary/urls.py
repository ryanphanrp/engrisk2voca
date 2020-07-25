from django.urls import path
from .views import HomePage

app_name = 'vocabulary'

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
]
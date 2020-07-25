from django.urls import path
from .views import HomePage

app_name = 'vocabulary'

urlpatterns = [
    path('home.php', HomePage.as_view(), name='home'),
]
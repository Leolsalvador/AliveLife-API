from .views import UserView
from django.urls import path


app_name = 'users'


urlpatterns = [
    path('login/', UserView.as_view(), name='login'),
]
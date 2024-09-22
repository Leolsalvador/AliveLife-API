from .views import UserView, VerifyTokenView
from django.urls import path


app_name = 'users'


urlpatterns = [
    path('login/', UserView.as_view(), name='login'),
    path('verify-token', VerifyTokenView.as_view(), name='verify-token')
]
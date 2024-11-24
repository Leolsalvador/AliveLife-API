from .views import UserView, VerifyTokenView, PatientListView
from django.urls import path


app_name = 'users'


urlpatterns = [
    path('login/', UserView.as_view(), name='login'),
    path('verify-token', VerifyTokenView.as_view(), name='verify-token'),
    path('patients/', PatientListView.as_view(), name='patient-list'),
    path('all/', UserView.as_view(), name='all-users'),
    path('create/', UserView.as_view(), name='create'),
]
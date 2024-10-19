from .views import DiagnosisView
from django.urls import path


app_name = 'diagnosis'


urlpatterns = [
    path('generate/', DiagnosisView.as_view(), name='generate'),
    path('generate/<int:id>/', DiagnosisView.as_view(), name='get_diagnosis'),
]

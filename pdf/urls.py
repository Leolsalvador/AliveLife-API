from pdf.views import FileView
from django.urls import path


app_name = 'pdf'


urlpatterns = [
    path('upload/', FileView.as_view(), name='upload'),
    path('list/', FileView.as_view(), name='list'),
    path('delete/', FileView.as_view(), name='delete'),
]
from pdf.views import FileView
from django.urls import path


app_name = 'pdf'


urlpatterns = [
    path('upload/', FileView.as_view(), name='upload'),
    path('upload/<int:id>', FileView.as_view(), name='uploadId'),
    path('list/', FileView.as_view(), name='list'),
    path('delete/<int:id>/', FileView.as_view(), name='delete'),
]
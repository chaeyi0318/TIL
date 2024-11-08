from django.urls import path
from . import views

app_name='weather'

urlpatterns = [
    path('', views.index, name='index'),
    path('save-data/', views.save_data, name='save_data'),
]

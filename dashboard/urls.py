from django.urls import path
from . import views

urlpatterns = [
    path('generate-dashboard/', views.generate_dashboard, name='generate_dashboard'),
]
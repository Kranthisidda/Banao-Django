from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('loginview/', views.loginview, name='loginview'),]





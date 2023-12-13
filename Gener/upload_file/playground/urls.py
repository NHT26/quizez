from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_and_run_scripts, name='upload_and_run_scripts'),
]
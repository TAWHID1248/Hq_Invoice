from django.urls import path
from Inv_App import views


app_name = 'Inv_App'


urlpatterns = [
    path('inv_form/', views.form_view, name='inv_form'),
    path('', views.home, name='home'),
    ]
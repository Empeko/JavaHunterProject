from django.urls import path

from . import views

app_name = 'vacancies'

urlpatterns = [
    path('', views.index, name='index'),
    path('demand/', views.demand, name='demand'),
    path('skills/', views.skills, name='skills'),
    path('hh_vacancies/', views.hh_vacancies, name='hh_vacancies'),
    path('geography/', views.geography, name='geography'),
]

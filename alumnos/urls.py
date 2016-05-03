from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^reportes/', views.hello_pdf, name='hello_pdf'),
    url(r'^$', views.inicio, name='inicio'),
    url(r'^alumnos/crear/', views.AlumnoCreateView.as_view(), name='create_alumnos'),
    url(r'^alumnos/', views.AlumnoListView.as_view(), name='list_alumnos'),
]

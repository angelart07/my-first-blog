from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^reportes/', views.hello_pdf, name='hello_pdf'),
    url(r'^docentes/crear/', views.DocenteCreateView.as_view(), name='create_docentes'),
    url(r'^docentes/', views.DocenteListView.as_view(), name='list_docentes'),
]

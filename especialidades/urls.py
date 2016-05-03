from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^reportes/', views.hello_pdf, name='hello_pdf'),
    url(r'^especialidades/crear/', views.EspecialidadCreateView.as_view(), name='create_especialidades'),
    url(r'^especialidades/', views.EspecialidadListView.as_view(), name='list_especialidades'),
]

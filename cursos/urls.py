from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^reportes/', views.hello_pdf, name='hello_pdf'),
    url(r'^cursos/crear/', views.CursoCreateView.as_view(), name='create_cursos'),
    url(r'^cursos/', views.CursoListView.as_view(), name='list_cursos'),
]

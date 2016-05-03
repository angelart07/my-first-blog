from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^reportes/', views.hello_pdf, name='hello_pdf'),
    url(r'^dependencias/crear/', views.DependenciaCreateView.as_view(), name='create_dependencias'),
    url(r'^dependencias/', views.DependenciaListView.as_view(), name='list_dependencias'),
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^reportes/', views.hello_pdf, name='hello_pdf'),
    url(r'^grados/crear/', views.GradoCreateView.as_view(), name='create_grados'),
    url(r'^grados/', views.GradoListView.as_view(), name='list_grados'),
]

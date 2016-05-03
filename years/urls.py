from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^reportes/', views.hello_pdf, name='hello_pdf'),
    url(r'^years/crear/', views.YearCreateView.as_view(), name='create_years'),
    url(r'^years/', views.YearListView.as_view(), name='list_years'),
]

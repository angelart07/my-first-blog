from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('alumnos.urls', namespace="alumnos")),
    url(r'^', include('cursos.urls', namespace="cursos")),
    url(r'^', include('dependencias.urls', namespace="dependencias")),
    url(r'^', include('docentes.urls', namespace="docentes")),
    url(r'^', include('especialidades.urls', namespace="especialidades")),
    url(r'^', include('grados.urls', namespace="grados")),
    url(r'^', include('notas.urls', namespace="notas")),
    url(r'^', include('years.urls', namespace="years")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
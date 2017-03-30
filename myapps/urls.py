from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	#linea que permite cargar archivo urls.py del proyecto album
	url(r'^album/',include('album.urls')),
    url(r'^admin/', admin.site.urls),
]

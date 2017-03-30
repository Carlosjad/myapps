from django.conf.urls import url
from album import views

urlpatterns = [
    url(r'^$', views.first_view, name='first_view'),

    #el name permite dspues tomar el valor desde un href
    url(r'^category/$', views.category, name='category_list'),

    #?P<cateogory_id>[0-9]+ es un parametro que se envia con una expresino regular cmo numero
    url(r'^category/(?P<category_id>[0-9]+)/detail/$', views.category_detail, name='category_detail'),	

    #views.PhotoListView.as_view() -> permite llamar la vista de forma automatica con el as_view a traves de la clase
    url(r'^photo/$', views.PhotoListView.as_view(), name='photo_list'),

    #pk es la llave primaria, esta sirve para ver detalladamente una imagen en especifica
    url(r'^photo/(?P<pk>[0-9]+)/detail/$', views.PhotoDetailView.as_view(), name='photo_detail'),	

    #pk es la llave primaria para el update
    url(r'^photo/(?P<pk>[0-9]+)/update/$', views.PhotoUpdateView.as_view(), name='photo_update'),	

    #pk es la llave primaria
    url(r'^photo/(?P<pk>[0-9]+)/delete/$', views.PhotoDeleteView.as_view(), name='photo_delete'),	
]
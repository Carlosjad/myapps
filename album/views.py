from django.shortcuts import render
from django.http import HttpResponse

"""forma para importar los modelos que se van a convertir en vistas"""
from album.models import Category, Photo

""" clases para listar y detallar """
from django.views.generic import ListView, DetailView
""" clases para crear, editar y eliminar """
from django.views.generic.edit import UpdateView,CreateView,DeleteView

"""permite redireccionar a una vista"""
from django.core.urlresolvers import reverse_lazy
# Create your views here.

#funcion que carga contenido html en la pagina
def first_view(request):
	return HttpResponse('<h1>Esta es mi primer vista</h1>')

#vista para las categorias
"""
permite crear las vistas para categoria

un objeto lista = modelo.objects.all() -> forma para django decirle que se haga un select * desde una tabla(modelo)
context= es un diccionario con las listas
se lo envia al template que se llama category dentro de album

"""
def category(request):
	category_list=Category.objects.all()
	context = {'object_list':category_list}
	return render(request, 'album/category.html', context);

"""
funccion que permite llamar los detalles de una categoria en especifico llamada por el id

recibe como parametro el identificador 
"""
def category_detail(request,category_id):
	category=Category.objects.get(id=category_id)
	context = {'object':category}
	return render(request, 'album/category_detail.html', context);


"""
clase para las fotos
se crea con vista basada en clase

cuando se define una clase y lo que esta en parentesis es una herencia
"""
class PhotoListView(ListView):
	"""doc string for PhotoListView"""
	model=Photo

"""
clase para listar y detallar una foto en especifico
"""
class PhotoDetailView(DetailView):
	model=Photo

"""clase para editar las fotos
	fields='__all__' -> sirve para que en el formulario se muestren todos los campos y se puedan editarlos todos

	esta clase hace que se llama automaticmante a un template llamado photo_form
"""
class PhotoUpdateView(UpdateView):
	model=Photo
	fields='__all__'

"""
clase que permite eliminar una foto
"""
class PhotoDeleteView(DeleteView):
	model=Photo
	success_url=reverse_lazy('photo_list')


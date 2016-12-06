from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.mascota.forms import MascotaForm
from app.mascota.models import Mascota
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.


def index(request):
    return render(request,'mascota/index.html')

#vistas basadas en funciones, aunque tambien existen las vistas basadas en clases (para versiones de django mayores a 1.6)
def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mascota:mascota_listar') #si el form es valido, este retornara al index de mascota (localizado en el urls de mascota)
    else:
        form = MascotaForm() #sino, se regresara nuevamente a la seccion de el formulario
    return render(request,'mascota/mascota_form.html',{'form':form}) #la clave va a ser el 'FORM' y el nombre de diccionario, es decir lo que esta despues de los dos puntos : sera el nombre del form la cual fue definido mas arriba la cual hace referencia a mascotaform


def mascota_list(request):
    mascota = Mascota.objects.all().order_by('id')
    contexto = {'mascotas':mascota}
    return render(request,'mascota/mascota_list.html', contexto)

def mascota_edit(request,id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'GET':
        form = MascotaForm(instance=mascota)
    else:
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('mascota:mascota_listar')
    return render(request,'mascota/mascota_form.html',{'form':form})

def mascota_delete(request, id_mascota):
    mascota = Mascota.objects.get(id=id_mascota)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascota:mascota_listar')
    return render(request, 'mascota/mascota_delete.html', {'mascota': mascota})

#vistas basadas en clases

class MascotaList(ListView):
    model = Mascota
    template_name = 'mascota/mascota_list.html'

class MascotaCreate(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota:mascota_listar')

class MascotaUpdate(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_form.html'
    success_url = reverse_lazy('mascota:mascota_listar')

class MascotaDelete(DeleteView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'mascota/mascota_delete.html'
    success_url = reverse_lazy('mascota:mascota_listar')
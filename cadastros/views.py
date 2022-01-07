from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from cadastros.forms import CidadeForm
from cadastros.models import Cidade

class BaseListView(ListView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'INATEL'
        return context

class CidadeList(BaseListView):

    queryset = Cidade.objects.all().order_by('nome')
    context_object_name = 'cidade'
    template_name = 'cadastros/lista_cidades.html'

class CidadeDetail(DetailView):

    queryset = Cidade.objects.all()
    context_object_name = 'cidade'
    template_name = 'cadastros/detalhe_cidades.html'

class CidadeDelete(DeleteView):

    model = Cidade
    context_object_name = 'cidade'
    template_name = 'cadastros/remove_cidades.html'
    success_url = reverse_lazy('cidades-list')

class CidadeCreate(CreateView):
    model = Cidade
    # fields = ['nome','capital'] Ou usa Field ou Form criado
    form_class = CidadeForm
    template_name = 'cadastros/cadastra_cidades.html'
    success_url = reverse_lazy('cidades-list')

class CidadeUpdate(UpdateView):
    model = Cidade
    form_class = CidadeForm
    template_name = 'cadastros/edita_cidades.html'
    success_url = reverse_lazy('cidades-list')

### Outra Forma de realizar CRUD por meio de funcoes ###

# class CidadeList(View):
#
#     def get(self, request):
#         qs = Cidade.objects.all().order_by('nome')
#
#         context = {
#             'cidades': qs,
#             'titulo': 'Inatel'
#         }
#
#         return render(request, 'cadastros/lista_cidades.html', context)
#
#     def post(self, request):
#         pass
#
# def lista_cidades(request):
#
#     qs = Cidade.objects.all().order_by('nome')
#
#     context = {
#         'cidades': qs,
#         'titulo': 'Inatel'
#     }
#
#     return render(request, 'cadastros/lista_cidades.html', context)
#
# def detalhe_cidade(request, id ):
#
#     ## id_cidade = request.GET['id_cidade']
#
#     ## cidade = Cidade.objects.get(pk=id_cidade)
#
#     cidade = get_object_or_404(Cidade, pk=id)
#
#     context = {
#         'cidade': cidade,
#         'titulo': 'Inatel'
#     }
#
#     return render(request, 'cadastros/detalhe_cidades.html', context)
#
# @login_required
# def cadastra_cidade(request):
#
#     if request.method == "POST":
#         form = CidadeForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return redirect('cidades-list')
#
#     else:
#         form = CidadeForm()
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'cadastros/cadastra_cidades.html',context)
#
# @login_required
# def remove_cidade(request, id):
#
#     cidade = get_object_or_404(Cidade, pk=id)
#
#     cidade.delete()
#
#     return redirect('cidades-list')
#
# @login_required
# def editar_cidade(request, id):
#
#     cidade = get_object_or_404(Cidade, pk=id)
#     form = CidadeForm(request.POST or None, instance=cidade)
#
#     if request.method == 'POST':
#         form = CidadeForm(request.POST, instance=cidade)
#         if form.is_valid():
#             form.save()
#             return redirect('cidades-list')
#
#     context = {
#         'form': form,
#         'obj': cidade,
#     }
#
#     return render(request, 'cadastros/edita_cidades.html', context)




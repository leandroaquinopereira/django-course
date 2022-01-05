from django.shortcuts import render

# Create your views here.
from cadastros.models import Cidade


def lista_cidades(request):

    qs = Cidade.objects.all()
    qs_capital = Cidade.objects.filter(capital=True)

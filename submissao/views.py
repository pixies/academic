#-*- encoding: utf-8 -*-
from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect
from submissao.models import Submissao
from submissao.forms import SubmissaoForm

# Create your views here.
def adcionar_submissao(request):
    form = SubmissaoForm(request.POST or None, request.FILES or None)
    submissao = Submissao.objects.filter(autor_id=request.user.membroprofile.id)
    #submissao = False
    print(submissao)
    print(len(submissao))

    print (form)

    if len(submissao) < 2:
        if form.is_valid():
            instance = form.save(commit=False)
            print (instance)
            instance.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/submissao')

    context = {
        'form': form,
    }

    return render(request, 'submissao/nova_submissao.html', context)

def listar_submissao(request):

    queryset = Submissao.objects.filter(autor_id=request.user.membroprofile.id)

    if request.user.is_authenticated():
        context = {
            'lista_resumos': queryset,
            "title": 'Minha Lista'
        }
    else:
        context = {
            "title": 'Lista'
        }
    return render(request, 'submissao/index.html', context)

def detalhes_submissao(request):
    context = {
        "title": 'Detalhes'
    }
    return render(request, 'submissao/index.html',context)

def editar_submissao(request):


    submissao = Submissao.objects.filter(autor_id=request.user.membroprofile.id)
    form = SubmissaoForm(request.POST or None, request.FILES or None, instance=submissao[0])
    #submissao = False

    if submissao:
        if form.is_valid():
            instance = form.save(commit=False)
            print (instance)
            instance.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/submissao')

    context = {
        'form': form
    }
    return render(request, 'submissao/editar_submissao.html', context)






'''
    queryset = Submissao.objects.filter(autor_id=request.user.membroprofile.id)

    if request.user.is_authenticated():

        form = SubmissaoForm(request.POST or None)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

        context = {
            "lista_resumos": queryset,
            "title": 'Minha Lista',
            "form": form
        }
    else:
        context = {
            "title": 'Lista'
        }

    return render(request, 'submissao/index.html', context)
'''




def deletar_submissao(request):
    return HttpResponse('deletar')

from django.shortcuts import render_to_response, RequestContext
from submissao.form import SubmissaoForm
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy
# Create your views here.
"""
def index_submissao(request):
    context = RequestContext(request)
    submissao_form = SubmissaoForm()

    if submissao_form.is_valid():
        submissao = submissao_form.save(commit=True)
        submissao.save()

        return HttpResponseRedirect('/')
    return render(request, 'submissao/index_submissao.html', {'form': submissao_form})




    #return HttpResponse(context)

"""

def nova_submissao(request):
    context = RequestContext(request)

    if request.method == 'POST':
        sub_form = SubmissaoForm(data=request.POST)

        if sub_form.is_valid():
            sub = sub_form.save()
            sub.save()
            return HttpResponseRedirect('/')

        else:
            print sub_form.errors
    else:
        sub_form = SubmissaoForm()
        print sub_form
    return render_to_response('submissao/index_submissao.html', {'sub_form': sub_form }, context)

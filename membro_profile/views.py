#-*- encoding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, RequestContext, render
from membro_profile.forms import MembroForm, MembroProfileForm, EditProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from membro_profile.models import MembroProfile

def some_view(request):
    if not request.user.is_authenticated():
        return HttpResponse("You are logged in.")
    else:
        return HttpResponse("You are not logged in.")



# Create your views here.
def register(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        membro_form = MembroForm(data=request.POST)
        membro_profile_form = MembroProfileForm(data=request.POST)

        if membro_form.is_valid() and membro_profile_form.is_valid():
            membro = membro_form.save()
            membro.set_password(membro.password)
            membro.save()

            membro_profile = membro_profile_form.save(commit=False)
            membro_profile.user = membro

            if 'avatar' in request.FILES:
                membro_profile.picture = request.FILES['avatar']

            membro_profile.save()
            registered = True
        else:
            print membro_form.errors, membro_profile_form.errors
    else:
        membro_form = MembroForm()
        membro_profile_form = MembroProfileForm()

    return render_to_response(
        'profile/register.html',
#        {'membro_form': membro_form, 'registered': registered},
        {'membro_form': membro_form, 'membro_profile_form': membro_profile_form, 'registered': registered},
        context)

def membro_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        membro = authenticate(username=username,password=password)

        if membro:
            if membro.is_active:
                login(request, membro)
                return HttpResponseRedirect('/profile/')
            else:
                return HttpResponse('Sua conta ainda não foi liberada.')
        else:
            print "Login e senha invalidos: {0}, {1}".format(username, password)
            return HttpResponse("Login ou Senha, Invalidos")
    else:
#        return render_to_response('profile/404.html', {}, context)
        return render_to_response('profile/login.html', {}, context)

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')


@login_required
def profile(request):
    context = RequestContext(request)
    usuario = User.objects.get(username=context['user'])
    membro = MembroProfile.objects.get(user=usuario)

    if membro:
        return render_to_response('profile/profile.html', {'m':membro}, context)
    else:
        return HttpResponse('Inscrição não encontrado')

from django.core.urlresolvers import reverse

@login_required
def edit_profile(request):
    membro = request.user
    form = EditProfileForm(
        request.POST or None,
        initial={
            'first_name': membro.first_name,
            'last_name': membro.last_name,
            'cpf': membro.membroprofile.cpf,
        }
    )

    if form.is_valid():
        membro.first_name = request.POST['first_name']
        membro.last_name = request.POST['last_name']
        membro.cpf = request.POST['cpf']

        membro.save()
        return HttpResponseRedirect('%s'%(reverse('profile')))

    context = {
        "form": form
    }

    return render(request, 'profile/editar.html', context)


def index(request):
    membro = 'AnonymousUser'
    context = RequestContext(request)
    if request.user.is_authenticated():
        membro = MembroProfile.objects.filter(user__username=request.user).latest('user').user
        context["membro"] = membro
        return render_to_response('profile/index.html', context)

    else:
        context["membro"] = membro
        return render_to_response('profile/index.html', context)
        #return HttpResponseRedirect('/register/')
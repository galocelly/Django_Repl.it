from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.http import  HttpResponseNotFound
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Count, Avg, Sum
from proy_java.models import *
from django.views.generic import TemplateView
from django.db.models import Q
from django.contrib.auth import login, logout
from django.contrib import auth as django_auth
from django.contrib.auth import login as auth_login
from django.core import *
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django import forms
from forms import Compilador
from forms import Test


#from django.contrib.formtools.wizard.views import SessionWizardView
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import *
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import requires_csrf_token

#from celery.result import AsyncResult

#from celery_test.tasks import do_something_long
#from django.core.urlresolvers import reverse
#from django.utils import simplejson as json
import itertools
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from registration import config
from registration.forms import RegistrationForm, LoginForm


class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm

    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super(LoginView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

    def get_success_url(self):
        try:
            return "/index/"
        except:
            return "/profile/"


class LogoutView(View):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LogoutView, self).dispatch(*args, **kwargs)

    def get(self, request):
        logout(request)
        return render(request, 'login.html')


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegistrationForm

    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(config.INDEX_REDIRECT_URL)
        else:
            return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):

        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
        )

        return super(RegisterView, self).form_valid(form)

    def get_success_url(self):
        return reverse('register-success')


class RegisterSuccessView(TemplateView):
    template_name = 'success.html'




# Create your views here.
def index(request):
    #dato = User.objects.all()
    if request.method=='POST':
        formulario = Compilador(request.POST, request.FILES)
       # formato = Test(request.POST)
        if formulario.is_valid():
            formulario.save()
            return render(request,'index.html',{'full_name':request.user.username, 'formulario':formulario})

        #if formato.is_valid():

         #   formato.id_codigo = formato.cleaned_data['id_codigo']
          #  formato.id_usuario = formato.cleaned_data['id_usuario']
           # formato.link = request.user.username
            #formato.cod_fuente = formato.cleaned_data['cod_fuente']
        #Test.save()
    else:
        formulario = Compilador()
        #formato =Test()
    return render(request,'index.html',{'full_name':request.user.username, 'formulario':formulario})
    

    #form = Compilado() {'full_name':request.user.username}  'formulario':formulario,
    #context = {"tittle": "unid" , "form":form}
    #if request.method == "POST":
     #   form = Compilador(request.POST)
      #3  if form.is_valid():
            #post = form.save(commit=False)
            #post.id_codigo = id_codigo
            #post.id_usuario = request.user.username
            #post.link = link
            #post.cod_fuente = cod_fuente
        #    post.save()
    #else:
     #   form = Compilador()

    #if request.method == "POST":
        #form = Compilador(request.POST)

        #if form.is_valid:
         #   id_codigo = form.cleaned_data['id_codigo']
          #  id_usuario = form.cleaned_data['id_usuario']
           # link = form.cleaned_data['link']
            #cod_fuente = form.cleaned_data['cod_fuente']
            #cod = Codigo()
            #cod.id_codigo = id_codigo
         #   cod.id_usuario = id_usuario
          #  cod.link = link
           # cod.cod_fuente = cod_fuente
           # cod.save()

       # form = Compilador()
        #ctx = {'form':form}
        #return render_to_response('index.html',{'full_name': request.user.username},ctx,request)

    #return render_to_response('index.html',{'full_name':request.user.username})
   # else:
    #    form = Compilador()
     #   ctx = {'form':form}
      #  return render_to_response('index.html',{'full_name': request.user.username})

    
def login(request):
    c = {}
    #c.update(csrf(request))    
    return render(request, 'login.html', c)


def auth(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = django_auth.authenticate(username=username, password=password)
    
    if user is not None:
        django_auth.login(request, user)
        return HttpResponseRedirect('logged/')
    else:
    	return HttpResponseRedirect('invalid/')

    
def logged(request):
    return render_to_response('index.html', 
                              {'full_name': request.user.username})

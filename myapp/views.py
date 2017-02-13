from myapp.forms import *
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from myapp.models import Codigos, AuthUser, Tipo
from myapp.serializers import CodigosSerializer, TipoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import time
from datetime import datetime
from django.utils.timezone import utc
 

# Create your views here.

import uuid

#def get_ref_id():
 #   referencia = str(uuid.uuid4())[:11].replace('-','').lower()
  #  try:
   #     id_exists = Codigos.objects.get(referencia=referencia)
    #    get_ref_id()
    #except:
     #   return referencia

#def share(request, referencia):
    #ref = Codigos.objects.get(referencia=referencia)
    #ref_url = settings.SHARE_URL + str(ref.referencia)
#   context = {'referencia':referencia,'ref_url':ref_url}
#   return render(request,'code.html',context)

def index(request):
    try:
        code_id = request.session['code_id_ref']
        obj = Codigos.objects.get(id_code=code_id)
    except:
        obj = None
    today = datetime.now() #fecha actual
    dateFormat = today.strftime("%Y/%m/%d") # fecha con formato
 
    hora=time.strftime("%H:%M:%S")
    fecha = dateFormat + " "+hora
    tipoop = 1
#convert string to datetime
   
    if request.method == 'POST':
        formulario = CodeForm(request.POST)
        #user = request.POST['user']
        code = request.POST['code']
        nombre_codigo = request.POST['nombre_codigo']
        user = AuthUser.objects.get(id=request.user.id)
        tipoop = request.POST['idtipo']
        
        if formulario.is_valid:
            form = formulario.save(commit=False)
            form.user = user
            form.referencia = fecha

            form.save()
            return HttpResponseRedirect('/index/')

#return HttpResponseRedirect('%s' %form.referencia)
    else:
        formul = CodeForm()

    context = {'formul':formul}   
    return render(request, 'index.html', context)
 
#@csrf_protect
@csrf_exempt
def reg(request):

    context = RequestContext(request)

    if request.method == 'POST':
        user_form = UserRegForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect('/index/login_user/')
    else:
        user_form = UserRegForm()

    return render_to_response('registration/registro.html', {'user_form': user_form}, context)

@csrf_exempt
def login_user(request):

    context = RequestContext(request)

    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/index/')
                else:
                    return HttpResponseRedirect('/index/')
            else:
                return HttpResponseRedirect('/index/login_user/')
    else:
        formulario = AuthenticationForm()
        
    return render_to_response('registration/login.html',{'formulario':formulario}, context)

@login_required(login_url='/login/')
def salir(request):
    logout(request)
    return HttpResponseRedirect('/index/')


#
class CodigosList(APIView):
    """
        List all snippets, or create a new snippet.
        """
    def get(self, request, format=None):
        snippets = Codigos.objects.all()
        print snippets
        serializer = CodigosSerializer(snippets, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CodigosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CodigosDetail(APIView):
    """
        Retrieve, update or delete a snippet instance.
        """
    def get_object(self, pk):
        try:
            return Codigos.objects.get(pk=pk)
        except Codigos.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CodigosSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CodigosSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TipoList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Tipo.objects.all()
        print snippets
        serializer = TipoSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TipoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

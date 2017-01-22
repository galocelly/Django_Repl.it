"""Java URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin, auth
from proy_java import views
admin.autodiscover()
import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index', views.index, name='index'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name="logout"),

                       # register
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^register/success/$',views.RegisterSuccessView.as_view(), name='register-success'),
    #url(r'^login/$', views.login, name='login'),
    #url(r'^auth/$', views.auth),
	#url(r'^auth/logged/$', views.logged),

    #url(r'^', views.login, name=''),
    #url(r'^register/$', include('registration.backends.default.urls')),
    #url(r'^register_success/', views.register_success),
 


]

if not settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
   
    urlpatterns += staticfiles_urlpatterns()
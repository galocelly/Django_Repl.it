from myapp import views
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from myapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
               #url(r'^(?P<referencia>.*)$', views.share, name='share'),
    url(r'^reg/$', views.reg, name='reg'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^salir/$', views.salir, name='salir'),
    
    url(r'^snippets/$', views.CodigosList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.CodigosDetail.as_view()),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)



# urlpatterns = [
#     url(r'^snippets/$', views.snippet_list),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

from django.conf.urls import patterns, include, url
from django.contrib import admin
from membro_profile import views
from submissao.views import nova_submissao
from django.conf import settings
from django.conf.urls.static import static

#from academic.views import index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'academic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', views.membro_login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^logout/$', views.user_logout, name='logout'),
    #url(r'^submissao/$', nova_submissao, name='submissao'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

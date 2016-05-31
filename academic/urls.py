from django.conf.urls import patterns, include, url
from django.contrib import admin
from membro_profile import views
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
)

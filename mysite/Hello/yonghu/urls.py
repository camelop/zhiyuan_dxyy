from django.conf.urls import url

from . import views

urlpatterns = [ 
    url(r'^$', views.problems, name='problems'), 
    url(r'^problems/$', views.problems, name='problems'), 
    url(r'^problem/(?P<problem_id>[0-9]+)/$', views.problem, name='problem'),
    url(r'^login/$', views.login, name='login'), 
    url(r'^logout/$', views.logout, name='logout'), 
    url(r'^unlock/$', views.unlock, name='unlock'), 
    url(r'^uhsnefoaijitnauyilnaug/$', views.submit, name='submit'), 
    url(r'^uhsnaidaij/$', views.addpoint, name='addpoint'), 
    url(r'^usehint/$', views.usehint, name='usehint'), 
]

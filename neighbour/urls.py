from django.conf.urls import url, include
from . import views

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url('^signup/$', views.signup, name='signup'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^hoods/',views.neighbourhood,name='neighbourhood'),
    url(r'^user/',views.user,name='user'),
    url(r'^business/',views.business,name='business'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^post/',views.post,name='post'),
    url(r'^neighborhood/(?P<pk>\d+)',views.neighbourhoods,name='neighborview')

]

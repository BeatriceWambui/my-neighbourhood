from django.conf.urls import url, include
from . import views

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url('^signup/$', views.signup, name='signup'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]
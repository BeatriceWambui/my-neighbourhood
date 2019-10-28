from django.conf.urls import url,include
from django.contrib.auth import views
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('neighbour.urls')),
]
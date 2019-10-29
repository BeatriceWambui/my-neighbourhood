from django.conf.urls import url,include
from django.contrib.auth import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('neighbour.urls')),
    url(r'^logout/$', views.logout, {"next_page": '/'}), 

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from .models import Profile,Businesses,My_User,Neighbourhood

# Register your models here.
admin.site.register(Profile)
admin.site.register(Businesses)
admin.site.register(My_User)
admin.site.register(Neighbourhood)

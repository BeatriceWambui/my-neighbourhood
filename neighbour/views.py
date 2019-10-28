from django.shortcuts import render,redirect
from django.http  import HttpResponse

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    return render(request,'blueprint/index.html')
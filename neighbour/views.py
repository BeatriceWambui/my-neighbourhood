from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import SignupForm,ProfileUpdateForm,UserUpdateForm,NeighbourhoodForm,UserForm,BusinessForm,PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Neighbourhood,My_User,Businesses,Post
from django.contrib import messages

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registration_form.html',{"form": form})

@login_required(login_url='/accounts/login/')
def index(request):
    hood = Neighbourhood.objects.all()
    return render(request,'blueprint/index.html',{'hood':hood})

@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context={
        'u_form': u_form,
        'p_form': p_form,
        'user':user
    }

    return render(request, 'blueprint/profile.html', context)

def ProfileDetailView(LoginRequiredMixin, DetailView):
   model = Profile

def neighbourhood(request):
    current_user = request.user
    posts = Post.objects.all()
    business = Businesses.objects.all()
    if request.method == 'POST':
        form = NeighbourhoodForm(request.POST,request.FILES)
        if form.is_valid():
            name=form.cleaned_data['name']
            location = form.cleaned_data['location']
            occupants = form.cleaned_data['occupants']
            saveHood = Neighbourhood(name=name,location=location,occupants=occupants)
            saveHood.save()
            return redirect(index)
    else:
        form = NeighbourhoodForm()
    return render(request,'blueprint/upload.html',{'form':form,'business':business,'posts':posts})

def user(request):
    current_user=request.user
    users = My_User.objects.all()
    if request.method == 'POST':
        user = current_user
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            user_id = form.cleaned_data['user_id']
            email = form.cleaned_data['email']
            saveUser = My_User(username=username,user_id=user_id,email=email)
            saveUser.save()
            return redirect(neighbourhood)
    else:
        form = UserForm()
    return render(request,'blueprint/users.html',{'form':form,'users':users})


def neighbourhoods(request,pk):
    specific_neighbourhood = Neighbourhood.objects.get(id=pk)
    neighbourhood_users = My_User.objects.filter(neighbourhood=specific_neighbourhood)
    context = {
        "neighbourhood_users":neighbourhood_users,
        "specific_neighbourhood":specific_neighbourhood
    }
    return render(request,"blueprint/specifichood.html",context)


def business(request):
    if request.method == 'POST':
        form2 = BusinessForm(request.POST,request.FILES)
        if form2.is_valid():
            business_name = form2.cleaned_data['business_name']
            business_email = form2.cleaned_data['business_email']
            saveBusiness = Businesses(business_name=business_name,business_email=business_email)
            saveBusiness.save()
            return redirect(neighbourhood)
    else:
        form2 = BusinessForm()
    return render(request,'blueprint/business.html',{'form2':form2})


def search_results(request):

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_business = Businesses.search_by_business_name(search_term)
        message = f"{search_term}"

        return render(request, 'blueprint/search.html',{"message":message,"business": searched_business})

    else:
        message = "You haven't searched for any term"
        return render(request, 'blueprint/search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request,'blueprint/post.html',{'form':form})
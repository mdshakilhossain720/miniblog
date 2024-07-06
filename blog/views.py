from django.shortcuts import render,HttpResponseRedirect
from .forms import Signupform,LoginForm
from django.contrib.auth import authenticate,login,logout
from .models import Post

# Create your views here.
def home(request):
    post=Post.objects.all()

    return render(request,'blog/home.html',{'posts':post})

#about
def about(request):
    return render(request,'blog/about.html')

#contract
def contract(request):
    return render(request,'blog/contact.html')

#dashboard
def dashboard(request):
    return render(request,'blog/dashboard.html')

#logout
def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/')

#contract
def userlogin(request):
    if not request.user.is_authenticated:

     if request.method == 'POST':
        form=LoginForm(request=request, data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data['username']
            upass=form.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/dashboard/')
     else:        
      fr=LoginForm()
     return render(request,'blog/login.html',{'fl':fr})
    
    else:
       return HttpResponseRedirect('/dashboard/')


#contract
def signup(request):
    if request.method == 'POST':
        fm=Signupform(request.POST)
        if fm.is_valid():
            fm.save()

    else:
     fm=Signupform()
    return render(request,'blog/signup.html',{'form':fm})

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required(login_url='/login')
def home(request):
    return render(request , 'home.html')
def signuppage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2: 
            messages.error(request,"password1 and password2 are not same !!!")
            return redirect("/") 
        
        else:
            
              my_user=User.objects.create_user(uname,email,pass1)
              my_user.save()
        #    print(uname,email,pass1,pass2)
              messages.success(request, "User is Successfully Registered !!!")
              return redirect("/login")
          
        
    return render(request,'signup.html')



def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('/home')
        else:
            messages.error(request,"Please Enter the Correct UserName and Password!!!")
            return redirect("/login")

    return render(request,'login.html')

def logoutpage(request):
    logout(request)
    return redirect('/login')
    
from django.core.checks.messages import Error
from django.db.utils import IntegrityError
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
def signnewuser(request):
    if request.method=='POST':
        if request.POST.get('password1')==request.POST.get('password2'):
            try:
               saveuser=User.objects.create_user(request.POST.get('username'),password=request.POST.get('password1'))
               saveuser.save()
               return render(request,'Signup.html',{'form':UserCreationForm(),'info': 'The User' + request.POST.get('username') + ' is Saved SuccessfullY!'})
            except IntegrityError:
                    return render(request,'Signup.html',{'form':UserCreationForm(),'info': 'The User' + request.POST.get('username') + ' is Already Exist!'})

        else:
            return render(request,'Signup.html',{'form':UserCreationForm(),'error': 'The Passwords Are Not Matching'})
    else:
        return render(request,'Signup.html',{'form':UserCreationForm})

def loginuser(request):
    if request.method=='POST':
        loginsuccess=authenticate(request,username=request.POST.get('username'),password=request.POST.get('password'))
        if loginsuccess is None:
             return render(request,'Login.html',{'form':AuthenticationForm(),'error': 'The Username & Passwords Are Wrong!'})
        else:
            login(request,loginsuccess)
            return redirect('Welcomepage')
    else:
        return render(request,'Login.html',{'form':AuthenticationForm()})

def Welcomepage(request):
    return render(request,'Welcome.html')


def Logoutpage(request):
    if request.method =='POST':
        logout(request)
        return redirect('loginuser')


from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


# Create your views here.


def signup(request):
    if request.method == "GET":
        signupForm = UserCreationForm()
        return render(request, 'users/signup2.html',{'signupForm': signupForm})

    elif request.method == "POST" :
        signupForm = UserCreationForm(request.POST)
        if signupForm.is_valid():
            signupForm.save()
            return redirect('/users/login')



def userlogin(request) :
    if request.method == "GET":
        loginForm = AuthenticationForm()
        return render(request, 'users/login.html',{'loginForm': loginForm})
    elif request.method == "POST" :
        loginForm = AuthenticationForm(request, request.POST)
        if loginForm.is_valid():    #검증단계
            login(request, loginForm.get_user())
            return redirect('/board/list')
        else :
            return redirect('/users/login')


def userlogout(request) :
    logout(request)
    return redirect('/users/login')
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def dash(request):
    return render(request, 'dash.html')

def regoPage(request):
    if request.method=='POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        
        if pass1 == pass2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already Used')
                return redirect('register')
            elif User.objects.filter(username=uname).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else:
                my_user = User.objects.create_user(uname, email, pass1)
                my_user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not the same')
            return redirect('register')
        
    return render(request, 'rego.html')



def loginPage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user=authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('dash')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:  
        return render(request, 'login.html')



def LogOutpage(request):
    logout(request)
    return redirect('login')
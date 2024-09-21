from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import userData
from .forms import signUp

def home(request):
    return render(request, 'home.html')

def cart(request):
    return render(request, 'cart.html')
        

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, "There was an error while logging in, Please try again.")
            return redirect('user_login')
            
    else:
        return render(request, 'userLogin.html')
    
def user_logout(request):
    logout(request)
    messages.success(request, "You have been Logged Out")
    return redirect('home')
    
def user_signup(request):
    if request.method == 'POST':
        form = signUp(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, "You Have Successfully Registered, Logging You in ....")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username= username, password= password)
            login(request, user)
            return redirect('home')
        
        else:
            messages.success(request, "Something went wrong, Please try again")
    else:
        form = signUp()
        return render(request, 'userSignUp.html', {'form': form})

    return render(request, 'userSignUp.html', {'form': form})

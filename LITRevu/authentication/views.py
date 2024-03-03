from django.shortcuts import render, redirect
from .forms import UserForm, SignInForm
from django.contrib.auth import authenticate, login


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')  # Redirect to login page after successful user creation
    else:
        form = UserForm
    return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page or any desired page after successful login.
                return redirect('success')
            else:
                # Handle invalid credentials
                error_message = "Invalid username or password."
                return render(request, 'signin.html', {'form': form, 'error_message': error_message})
    else:
        form = SignInForm()
    return render(request, 'signin.html', {'form': form})


def logout(request):
    return render(request, 'logout.html')


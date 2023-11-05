from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Login view
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page based on the user's profile status.
            if user.profile.is_admin:
                return redirect('admin_dashboard')
            elif user.profile.is_responsable:
                return redirect('responsable_dashboard')
            elif user.profile.is_pompiste:
                return redirect('pompiste_dashboard')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'users/login.html', {'error': 'Invalid login'})
    else:
        return render(request, 'users/login.html')

# Logout view
@login_required
def user_logout(request):
    logout(request)
    return redirect('user_login')

# Registration view
def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        statut = request.POST['statut']

        if password == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'users/register.html', {'error': 'Username already exists'})
            else:
                user = User.objects.create(username=username, password=make_password(password))
                Profile.objects.create(user=user, statut=statut)
                return redirect('user_login')
        else:
            return render(request, 'users/register.html', {'error': 'Passwords do not match'})
    else:
        return render(request, 'users/register.html')

# Protected view example
@login_required
def some_view(request):
    if hasattr(request.user, 'profile') and request.user.profile.is_responsable:
        # Do something for responsable
        return HttpResponse("You are a responsable.")
    else:
        return HttpResponse("You are not authorized to view this page.")

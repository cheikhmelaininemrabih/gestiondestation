from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from station.models import Station

@login_required
def responsable_dashboard(request):
    
    try:
        station = request.user.managed_station.get()
    except Station.DoesNotExist:
        station = None

    context = {
        'station': station,
    }
    return render(request, 'dashboard/responsable_dashboard.html', context)

def admin_dashboard(request):
    stations = Station.objects.all()  # Retrieve all stations
    return render(request, 'users/admin_dashboard.html', {'stations': stations})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            if user.profile.is_admin:
                return redirect('station:station_list')
            elif user.profile.is_responsable:
                return redirect('/cuve')
            elif user.profile.is_pompiste:
                return redirect('pompe:pompe_list')
        else:
            
            return render(request, 'users/login.html', {'error': 'Invalid login'})
    else:
        return render(request, 'users/login.html')

# Logout view
@login_required
def user_logout(request):
    logout(request)
    return redirect('user_login')


def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        tel = request.POST.get('tel')
        nom = request.POST.get('nom')
        statut = int(request.POST.get('statut'))

        # Validate that all required fields are provided
        if not all([username, password, password2, tel, nom]):
            return render(request, 'users/register.html', {'error': 'All fields are required.'})

        if password == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'users/register.html', {'error': 'Username already exists'})
            else:
                # Create the User instance and hash the password
                user = User.objects.create(username=username)
                user.set_password(password)  # Properly handle hashing
                user.save()  # Save the user to the database

                # Create the associated Profile instance
                Profile.objects.create(user=user, tel=tel, nom=nom, statut=statut)

                # Optionally, authenticate and log the user in after creating the account
                 #new_user = authenticate(username=username, password=password)
                #if new_user is not None:
                #     login(request, new_user)
                
                return redirect('user_login')  # Redirect to the login page after registration
        else:
            return render(request, 'users/register.html', {'error': 'Passwords do not match'})
    else:
        return render(request, 'users/register.html')


# Protected view example
@login_required
def some_view(request):
    if hasattr(request.user, 'profile') and request.user.profile.is_responsable:
        
        return HttpResponse("You are a responsable.")
    else:
        return HttpResponse("You are not authorized to view this page.")

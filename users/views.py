from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from station.models import Station
from .decorator import active_and_role_required
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import re
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
    stations = Station.objects.all()  
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

@login_required
def user_logout(request):
    logout(request)
    return redirect('user_login')



def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        nom = request.POST.get('nom')
        tel = request.POST.get('tel')
        statut = int(request.POST.get('statut', '0'))

       
        try:
            validate_email(username)
            is_email = True
        except ValidationError:
            is_email = False

      
        is_telephone = re.match(r'^\+?1?\d{9,15}$', username)

        if not is_email and not is_telephone:
            return render(request, 'users/register.html', {'error': 'Enter a valid email or telephone number.'})

        
       

        if not all([username, password, password2, tel, nom]):
            return render(request, 'users/register.html', {'error': 'All fields are required.'})

        if password != password2:
            return render(request, 'users/register.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'users/register.html', {'error': 'Username already exists'})

        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        Profile.objects.create(user=user, tel=tel, nom=nom, statut=statut, is_active=False)

        return redirect('user_login')
    else:
        return render(request, 'users/register.html')

@login_required
def admin_activate_user(request, user_id):
    if not request.user.profile.is_admin:
        return HttpResponse("Unauthorized", status=401)

    try:
        user_to_activate = User.objects.get(pk=user_id)
        user_to_activate.profile.is_active = True
        user_to_activate.profile.save()
    except User.DoesNotExist:
        return HttpResponse("User does not exist.", status=404)

    return redirect('admin_user_activation_list')

@login_required
def dashboard(request):
    if request.user.profile.is_admin:
        stations = Station.objects.all()
        return render(request, 'dashboard/admin_dashboard.html', {'stations': stations})
    elif request.user.profile.is_responsable and request.user.profile.is_active:
        try:
            station = request.user.managed_station.get()
        except Station.DoesNotExist:
            station = None
        return render(request, 'dashboard/responsable_dashboard.html', {'station': station})
    elif request.user.profile.is_pompiste and request.user.profile.is_active:
        
        return render(request, 'dashboard/pompiste_dashboard.html')
    else:
       
        return HttpResponse("Your account is not activated or you do not have a role assigned.")

@login_required
@active_and_role_required('responsable')
def responsable_dashboard(request):
    try:
       
        station = request.user.profile.managed_station
    except Station.DoesNotExist:
        station = None

    context = {
        'station': station,
    }
    return render(request, 'dashboard/responsable_dashboard.html', context)
@login_required
def some_view(request):
    if hasattr(request.user, 'profile') and request.user.profile.is_responsable:
        
        return HttpResponse("You are a responsable.")
    else:
        return HttpResponse("You are not authorized to view this page.")

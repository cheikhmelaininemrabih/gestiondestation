from audioop import reverse
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from pompe.models import Pompe
from cuve.models import Cuve
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from pompiste.models import Pompiste
from cuve.models import Cuve
from station.models import Station
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from station.models import Station
from .decorator import active_and_role_required
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework import status
import json
from django.views.decorators.csrf import csrf_exempt

import re
from django.urls import reverse

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


@login_required
def delete_user(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        if user:
            user.delete()
            messages.success(request, 'Utilisateur supprimé avec succès.')
        else:
            messages.error(request, 'Utilisateur non trouvé.')
    except User.DoesNotExist:
        messages.error(request, 'Utilisateur non trouvé.')

    # Corrected reverse usage
    return HttpResponseRedirect(reverse('dashboard'))

@login_required(login_url='sing_in')
def dashboard(request):
    # Fetch only inactive users
    all_users = User.objects.all()  # Fetch all users
    inactive_users = User.objects.filter(is_active=False)  # Fetch only inactive users
    all_stations = Station.objects.all()
    all_pompistes = Pompiste.objects.all()
    all_pompes = Pompe.objects.all() 
    all_cuves = Cuve.objects.all()
    responsables = Profile.objects.filter(role='responsable').select_related('user')
    # pompistes = Profile.objects.filter(role='pompiste')


    context = {
        'all_users': all_users,
        'inactive_users': inactive_users,  # Add this to your context
        'all_stations': all_stations,
        'all_pompistes': all_pompistes,
        'all_pompes': all_pompes,
        'all_cuves': all_cuves,
        'responsables': responsables,
        # 'pompistes': pompiste,
    }
    return context;

def assign_pompiste_to_station(request, station_id):
    station = get_object_or_404(Station, pk=station_id)
    pompistes = Pompiste.objects.filter(is_active=True)

    if request.method == 'POST':
        pompiste_id = request.POST.get('pompiste')
        pompiste = get_object_or_404(Pompiste, id=pompiste_id)
        pompiste.station = station  # Assuming Pompiste model has a 'station' field
        pompiste.save()
        return redirect('station:station_detail', pk=station_id)

    return render(request, 'users/responsable_dashbord.html', {'station': station, 'pompistes': pompistes})


def add_pompe_to_station(request, station_id):
    station = Station.objects.get(pk=station_id)
    cuves = Cuve.objects.filter(id_station=station)
    if request.method == 'POST':
        cuve_id = request.POST.get('cuve')
        type = request.POST.get('type')
        cuve = Cuve.objects.get(pk=cuve_id)
        pompe = Pompe.objects.create(type=type, id_cuve=cuve)
        return redirect('users:responsable_dashbord')  

    return render(request, 'users/responsable_dashbord.html', {'cuves': cuves, 'station_id': station_id})


def add_cuve_to_station(request, station_id):
    station = get_object_or_404(Station, id=station_id)
    if request.method == 'POST':
        cuve = Cuve()
        cuve.charge = request.POST.get('charge')
        cuve.stocke = request.POST.get('stocke')
        cuve.Qt_min = request.POST.get('Qt_min')
        cuve.id_station = station
        
        cuve.save()
        return redirect('responsable_dashbord')
    return render(request, 'add_cuve_to_station', {'station': station})
def responsable_dashbord(request):
    try:
        profile = Profile.objects.get(user=request.user)
        stations = Station.objects.filter(responsables=profile)
        for station in stations:  
            station.pompistes_data = []
            pompistes = Pompiste.objects.filter(station=station)
            for pompiste in pompistes:
                pompes_assigned_to_pompiste = Pompe.objects.filter(id_pompiste=pompiste)
                station.pompistes_data.append({'pompiste': pompiste, 'pompes': pompes_assigned_to_pompiste})

            station.cuves_data = []
            cuves = Cuve.objects.filter(id_station=station)
            for cuve in cuves:
                pompes_related_to_cuve = Pompe.objects.filter(id_cuve=cuve)
                station.cuves_data.append({'cuve': cuve, 'pompes': pompes_related_to_cuve})
            station.pompes = Pompe.objects.filter(id_cuve__in=cuves)

    except Profile.DoesNotExist:
        stations = None

    context = {'stations': stations}
    return render(request, 'users/responsable_dashbord.html', context)

def pompiste_dashbord(request):
    return render(request, 'users/pompiste_dashbord.html')


@csrf_exempt
def alloo(request):
    data= json.loads(request.body.decode('utf-8'))
    num1=data.get('num1',0)
    num2=data.get('num2',0)
    return JsonResponse({'num1':num1,"num2":num2})


@csrf_exempt
def sing_in(request):
    # if request.method == "GET":
    #     return HttpResponse("Hello")

    if request.method == "POST":
        try:
            data = json.loads(request.body.decode('utf-8'))
            num1 = data.get('num1', 0)
            num2 = data.get('num2', 0)
            return JsonResponse({'num1': num1, 'num2': num2})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    return HttpResponse("Invalid request method")


@csrf_exempt
def sing_in(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        username = data.get('email', 0)
        password = data.get('password', 0)
        succeus=False
        try:
            profile = Profile.objects.get(tel=username)
            user=User.objects.get(id=profile.user_id)
            authenticated_user = authenticate(request, username=user.username, password=password)
            
                
            if authenticated_user:
                succeus=True
                login(request, authenticated_user)
                if profile.role == 'admin':
                    return JsonResponse({'role':"admin","succeus":succeus})
                elif profile.role == 'responsable':
                    print("authenticated_user==============",authenticated_user)
                    return JsonResponse({'role':"responsable","succeus":succeus})
                elif profile.role == 'pompiste':
                    return JsonResponse({'role':"pompiste","succeus":succeus})
                else:
                    messages.error(request, "Your account doesn't have a role assigned. Please contact admin.")
                    return redirect('sing_in')
            else:
                return JsonResponse({'role':"non","succeus":succeus})
        except Profile.DoesNotExist:
            messages.error(request, "User with this phone number does not exist.")
            return JsonResponse({'role':"non","succeus":succeus})

    return HttpResponse("this method it is not a post")

@csrf_exempt
def sing_up(request):
    error = False
    message = ""
    succeus=False
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        name = data.get('username', 0)
        email = data.get('email', 0)
        password = data.get('password', 0)
        # repassword = data.get('password_repeat', 0)
        tel = data.get('tel', 0)
        # Email
        # try:
        #     validate_email(email)
        # except:
        #     error = True
        #     message = "Enter un email valide svp!"
        # password
        # if error == False:
        #     if password != repassword:
        #         error = True
        #         message = "Les deux mot de passe ne correspondent pas!"
        # Exist
        user = User.objects.filter(Q(email=email) | Q(username=name)).first()
        if user:
            error = True
            message = f"Un utilisateur avec email {email} ou le nom d'utilisateur {name} exist déjà'!"

        # register
        if not error:
            succeus=True
            user = User(
                username=name,
                email=email,
            )
            user.save()

            user.password = password
            user.set_password(user.password)
            user.is_active = False
            user.save()
            profile = Profile(user=user, tel=tel, role="None")
            profile.save()
            # return redirect('sing_in')
            message="use is saved successfully"
            return JsonResponse({'msg':message,"succeus":succeus})
    context = {
        'error': error,
        'message': message
    }
    return JsonResponse({'msg':message,"succeus":succeus})
    # return render(request, 'users/register.html', context)

import logging

logger = logging.getLogger(__name__)
def activate_user(request, user_id):
    user_to_activate = User.objects.get(pk=user_id)

    user_to_activate.is_active = True
    user_to_activate.save()
    profile, created = Profile.objects.get_or_create(user=user_to_activate)
    profile.is_active = True
    profile.save()
    return redirect('dashboard')

def role_user(request, user_id):
    user = User.objects.get(pk=user_id)
    roles = ['admin', 'responsable', 'pompiste']

    if request.method == 'POST':
        selected_role = request.POST.get('selected_role')
        if selected_role in roles:
            profile, created = Profile.objects.get_or_create(user=user)
            profile.role = selected_role
            profile.save()
            return redirect('dashboard')

    context = {
        'user': user,
        'roles': roles,
    }
    return render(request, 'users/role_user.html', context)


@login_required
def modify_user(request, user_id):
   
    user_to_modify = get_object_or_404(User, pk=user_id)

    if request.method == 'POST':
       
        user_to_modify.username = request.POST.get('username')
        user_to_modify.email = request.POST.get('email')
        user_to_modify_tel = request.POST.get('tel')
        
        
        
        password = request.POST.get('password')
        if password:
            user_to_modify.set_password(password)

       
        user_to_modify.save()
        messages.success(request, 'User details updated successfully.')
        return redirect('dashboard')  

    context = {
        'user': user_to_modify
    }
    return render(request, 'users/modify_user.html', context)


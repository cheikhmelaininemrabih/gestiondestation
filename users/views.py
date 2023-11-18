from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from pompe.models import Pompe
from cuve.models import Cuve
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
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


import re
@login_required(login_url='sing_in')

def dashboard(request):
    all_users = User.objects.filter(is_active=False)
    context = {
        'all_users': all_users
    }
    return render(request, 'users/admin_dashbord.html', context)


def responsable_dashbord(request):
    try:
        profile = Profile.objects.get(user=request.user)
        stations = Station.objects.filter(responsables=profile)
    except Profile.DoesNotExist:
        stations = None

    context = {'stations': stations}
    return render(request, 'users/responsable_dashbord.html', context)

def pompiste_dashbord(request):
    return render(request, 'users/pompiste_dashbord.html')

def sing_in(request):
    if request.method == "POST":
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        user = User.objects.filter(email=email).first()
        if user:
            auth_user = authenticate(username=user.username, password=password)
            if auth_user:
                login(request, auth_user)
                try:
                    profile = Profile.objects.get(user=auth_user)
                    role = profile.role
                except Profile.DoesNotExist:
                    print("Le profil de l'utilisateur n'existe pas")
                    return redirect('login')

                if role == 'admin':
                    return redirect('dashboard')
                elif role == 'responsable':
                    return redirect('responsable_dashbord')
                elif role == 'pompiste':
                    return redirect('pompiste_dashbord')
                else:
                    print("compte ne pas valide")
            else:
                print("Mot de passe incorrect")
        else:
            print("L'utilisateur n'existe pas")

    return render(request, 'users/login.html', {})

def sing_up(request):
    error = False
    message = ""
    if request.method == "POST":
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        repassword = request.POST.get('repassword', None)
        tel = request.POST.get('tel', None)
        # Email
        try:
            validate_email(email)
        except:
            error = True
            message = "Enter un email valide svp!"
        # password
        if error == False:
            if password != repassword:
                error = True
                message = "Les deux mot de passe ne correspondent pas!"
        # Exist
        user = User.objects.filter(Q(email=email) | Q(username=name)).first()
        if user:
            error = True
            message = f"Un utilisateur avec email {email} ou le nom d'utilisateur {name} exist déjà'!"

        # register
        if error == False:
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
            return redirect('sing_in')
    context = {
        'error': error,
        'message': message
    }
    return render(request, 'users/register.html', context)


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




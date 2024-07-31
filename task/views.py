from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User

from Banano_django import settings
from .forms import CustomUserCreationForm, ProfileForm

def register(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            if not hasattr(user, 'profile'):
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
            else:
                profile = user.profile
                profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
                profile_form.save()

            return redirect('loginview')
    else:
        user_form = CustomUserCreationForm()
        profile_form = ProfileForm()

    return render(request, 'task/register.html', {'user_form': user_form, 'profile_form': profile_form})
def loginview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
        
            login(request, user)
            
            if user.profile.user_type == 'patient':
                return redirect('patient_dashboard')
            else:
                return redirect('doctor_dashboard')
    else:
        return render(request,'task/login.html')

def patient_dashboard(request):
    return render(request, 'task/patient_dashboard.html')

def doctor_dashboard(request):
    return render(request, 'task/doctor_dashboard.html')






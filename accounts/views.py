from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import User, Profile


def home(request):
    title = 'Fingerprint Attendance'
    return render(request, 'accounts/home.html', {'user': request.user, 'title': title})


def register(request, *args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login')
    context = {
        'form': form
    }
    return render(request, "accounts/register.html", context)


@login_required
def profile(request):
    title = 'User Profile'
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
        context = {
            'user': user,
            'title': title
        }
        return render(request, 'accounts/profile.html', context)
    except:
        profile = Profile.objects.create(user=user)
        context = {
            'user': user,
            'title': title
        }
        return render(request, 'accounts/profile.html', context)


@login_required
def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': u_form,
        'profile_form': p_form
    }

    return render(request, 'accounts/edit_profile.html', context)
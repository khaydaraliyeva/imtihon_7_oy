from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from app.models import UserProfile
from app.forms import UserProfileForm, LoginForm, UserForm


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm, UserProfileForm


def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            # profile.status = 'client'  # This line can be commented out as status is set by default
            profile.save()

            user = authenticate(username=user_form.cleaned_data['username'],
                                password=user_form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('client-index')
            else:
                return render(request, 'register.html', {
                    'user_form': user_form,
                    'profile_form': profile_form,
                    'error': 'User authentication failed.'
                })
        else:
            return render(request, 'register.html', {
                'user_form': user_form,
                'profile_form': profile_form,
                'error': 'Form is invalid.',
                'user_form_errors': user_form.errors,
                'profile_form_errors': profile_form.errors
            })
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return after_login(request)
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password'})
        else:
            return render(request, 'login.html', {'form': form, 'error': 'Invalid form submission'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {"form": form})


def after_login(request):
    user = UserProfile.objects.get(user=request.user)
    if user.status == 'admin':
        return render(request, 'admin1/request.html')
    elif user.status == 'seller':
        return render(request, 'seller/request.html')
    else:
        return redirect('client-index')


def user_logout(request):
    logout(request)
    return redirect('client-index')
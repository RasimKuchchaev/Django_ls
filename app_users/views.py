from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from app_users.forms import AuthForm, ExtendedRegisterForm
from django.contrib.auth.views import LoginView, LogoutView


def login_view(request):
    if request.method == 'POST':
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Вы успешно вошли в систему")
                else:
                    auth_form.add_error('__all__', 'Учетная запись пользователя не активна!')
            else:
                auth_form.add_error('__all__', 'Ошибка! Проверте правильность написания логина и пароля')
    else:
        auth_form = AuthForm()
        context = {
            'form': auth_form
        }
        return render(request, 'users/login.html', context=context)


class AnotherLoginView(LoginView):
    template_name = 'users/login.html'

class AnotherLogoutView(LogoutView):
    # template_name = 'users/logout.html'
    next_page = '/'

def logout_view(request):
    logout(request)
    return HttpResponse("Вы вышли из учетки")

def register_view(request):
    print("register_view")
    if request.method == 'POST':
        print("POST")
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("is_valid")
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def another_register_view(request):
    print("register_view")
    if request.method == 'POST':
        print("POST")
        form = ExtendedRegisterForm(request.POST)
        if form.is_valid():
            print("is_valid")
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = ExtendedRegisterForm()
    return render(request, 'users/register.html', {'form': form})
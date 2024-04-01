from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, ChangePasswordForm


def show_alert(request):
    return render(request, 'auth_app/alert.html')


@login_required
def list_users(request):
    pass


@login_required
def show_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        user = User.objects.get(id=request.user.id)
        user.first_name = first_name.capitalize()
        user.last_name = last_name.capitalize()
        user.email = email.lower()
        user.save()
        return redirect('home_page')

    return render(request, 'auth_app/profile.html')


@login_required
def add_user(request):
    context = {}
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        # print(f'{fname} {lname} {user_name} {email} {passwd} {repasswd}')
        if password == re_password:
            # print('valid')
            new_user = User.objects.create_user(username, email, password)
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.save()

            return redirect('home_page')
        else:
            context = {
                'message': 'Паролі не співпадають!',
                'color': 'alert-danger'
            }

    return render(request, 'auth_app/add_user.html', context)


@login_required
def delete_user(request):
    pass


@login_required
def change_password(request):
    context = {}
    if request.method == 'POST':

        form = ChangePasswordForm(request.POST)

        if form.is_valid():

            current_password = request.POST.get('current_password')
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')

            if new_password == confirm_password:
                user = User.objects.get(id=request.user.id)
                check_password = user.check_password(current_password)
                if check_password:
                    user.set_password(new_password)
                    user.save()
                    return redirect('home_page')
                else:
                    context = {
                        'message': 'Неправильний текучий пароль!',
                        'color': 'alert-danger'
                    }
            else:
                context = {
                    'message': 'Паролі не співпадають!',
                    'color': 'alert-danger'
                }

    else:
        form = ChangePasswordForm()

    context['form'] = form
    return render(request, 'auth_app/change_password.html', context)


def login_user(request):
    context = {}
    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            remember_me = request.POST.get('remember_me')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Exp session 5 min
                if remember_me != 'on':
                    request.session.set_expiry(300)
                login(request, user)
                return redirect('home_page')
            else:
                # return HttpResponse('Error, user not exists.')
                context = {
                    'message': 'Невірний користувач або пароль!',
                    'color': 'alert-danger'
                }
    else:
        form = LoginForm()

    # return render(request, 'auth_app/login.html', {'form': form})
    context['form'] = form  # Додати форму до контексту для передачі у шаблон
    return render(request, 'auth_app/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('auth_app:login_page')


def test(request):
    return render(request, 'auth_app/test.html')

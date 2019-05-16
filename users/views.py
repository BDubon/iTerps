from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect_url = request.POST.get('next', 'home')
            return redirect(redirect_url)
        else:
            messages.error(request, 'Bad username or password')

        if 'next' in request.POST:
            return redirect(request.POST.get('next'))
        else:
            return redirect('home')
    # context = {'form': form}
    return render(request, 'users/login.html', {})


def logout_user(request):
    logout(request)

    return redirect('next')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account Has Been Created! Log In!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')


"""
TYPES of MESSAGES
messages.debug
messages.info
messages.success
messages.warning
messages.error
"""




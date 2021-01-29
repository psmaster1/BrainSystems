from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UserCreateForm, UserUpdateForm, ContactForm
from .models import PageSettings


def get_page_settings(page):
    page_settings = PageSettings.objects.filter(page=page)
    if page_settings:
        return page_settings.get()
    return ''


def index(request):
    return render(request, 'web/index.html', {'page_settings': get_page_settings('Index')})


def register_view(request):
    register_form = UserCreateForm()
    if request.method == 'POST':
        register_form = UserCreateForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse('web:backend'))
    return render(request, 'web/register.html',
                  {'register_form': register_form, 'page_settings': get_page_settings('Register')})


def impressum(request):
    return render(request, 'web/impressum.html')


def datenschutz(request):
    return render(request, 'web/datenschutz.html')


def login_view(request):
    login_form = AuthenticationForm()
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse('web:backend'))
    return render(request, 'web/login.html', {'login_form': login_form, 'page_settings': get_page_settings('Login')})


def logout_view(request):
    logout(request)
    return redirect(reverse('web:index'))


def kontakt(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Wir haben Ihre Nachricht erhalten! Wir werden uns in kürze bei Ihnen melden. Danke!')
            return redirect('web:kontakt')

    else:
        form = ContactForm()
    return render(request, 'web/kontakt.html', {'form': form, 'page_settings': get_page_settings('Contact')})


@login_required
def backend(request):
    return render(request, 'web/users/backend-index.html')


@login_required
def userdata(request):
    if request.method == 'POST':
        form = UserUpdateForm(data=request.POST, instance=request.user)
        if form.is_valid():
            messages.success(request, 'Änderungen wurden erfolgreich gespeichert!')
            form.save()
            return redirect('web:userdata')
    else:
        form = UserUpdateForm(instance=request.user)

    return render(request, 'web/users/user-data.html', {'form': form})


@login_required
def chatbot(request):
    return render(request, 'web/users/chatbot.html')

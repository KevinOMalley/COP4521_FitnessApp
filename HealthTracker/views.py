from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from HealthTracker.models import Account, UserHealth
from .forms import RegisterForm, AuthenticationForm, HealthForm

def register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse("You are already authenticated.")

    context = {}
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            #form.save implicitly calls create_user which saves an instance of object to database
            form.save()
            print("User saved successfully.")
            username = form.cleaned_data.get('username')
            UserModel = get_user_model()
            user = UserModel._default_manager.get(username=username)
            login(request, user)
            return redirect('index')
        else:
            for field in form:
                print("Field Error:", field.name,  field.errors)

            context['registration_form'] = form
    else:
        form = RegisterForm()
        context['registration_form'] = form

    return render(request, 'registration/register.html', context)

def index(request):
    template = loader.get_template("HealthTracker/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def about(request):
    return render(request, 'HealthTracker/about.html')

def login_view(request, *args, **kwargs):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("profile")

    if request.POST:
        form = AuthenticationForm(request.post)
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username, password)
            if user is not None:
                login(request, user)
                return redirect("profile")
    else:
        form = AuthenticationForm()

    context['form'] = form
    return render(request, "registration/login.html")

def logout_view(request):
    logout(request)
    return redirect("index")

@login_required
def user_profile(request):
    user = request.user
    account = Account.objects.get(username=user.username)
    context = {
        'account': account,
    }
    return render(request, "HealthTracker/user_profile.html", context)

@login_required
def health_info(request):
    user = request.user
    try:
        health_info = UserHealth.objects.get(user=user)
    except UserHealth.DoesNotExist:
        health_info = None
    if request.POST:
        form = HealthForm(request.POST, instance=health_info)
        if form.is_valid():
            health_data = form.save(commit=False)
            health_data.username_id = user.username
            health_data.save()
    else:
        form = HealthForm(instance=health_info)

    context = {
        'health_info': health_info,
        'form': form,
    }
    return render(request, 'HealthTracker/health_info.html', context)
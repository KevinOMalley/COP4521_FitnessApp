from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from HealthTracker.models import Account
from .forms import RegisterForm

def register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated: 
        return HttpResponse("You are already authenticated as " + str(user.email))

    context = {}
    if request.POST:
        form = RegisterForm(request.POST)
        print("Form is being processed...")
        if form.is_valid():
            print("Form is valid. Saving...")
            
            form.save()
            print("User saved successfully.") 
            
            email = form.cleaned_data.get('email').lower()
            username = form.cleaned_data.get('username')
            UserModel = get_user_model()
            user = UserModel._default_manager.get(username=username)
            login(request, user)
            return redirect('index')
        else:
            print("form is not valid")
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

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index.html')
        else:
            error_message = 'Invalid credentials'
            return render(request, 'registration/login.html', {'error_message': error_message})
    else:
        return render(request, 'registration/login.html')

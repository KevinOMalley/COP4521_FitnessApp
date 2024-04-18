from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from django.template import loader
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from HealthTracker.models import Account, UserHealthInfo, MyAccountManager
from .forms import RegisterForm, AuthenticationForm, HealthInfoForm

def register_view(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse("You are already authenticated.")

    context = {}
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            print("User saved successfully.")
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            is_under_18 = form.cleaned_data.get('is_under_18')

            user = Account.objects.create_user(email=email, username=username, is_child=is_under_18, password=password)

            login(request, user)
            return redirect('index')
        else:
            for field in form:
                print("Field Error:", field.name,  field.errors)

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
def userHome(request):
    user = request.user
    account = Account.objects.get(username=user.username)
    context = {
        'account': account,
    }
    return render(request, "HealthTracker/user_page/user_home.html", context)

@login_required
def workoutTracker(request):
    user = request.user
    account = Account.objects.get(username=user.username)

    if account.is_child:
        context = {
            'message': "This feature is not available for users under 18"
        }
        return render(request, "HealthTracker/user_page/tracker_pages/forbidden.html", context)
    
    context = {
        'account': account,
    }
    return render(request, "HealthTracker/user_page/tracker_pages/workout_tracker.html", context)

@login_required
def sleepTracker(request):
    user = request.user
    account = Account.objects.get(username=user.username)
    context = {
        'account': account,
    }
    return render(request, "HealthTracker/user_page/tracker_pages/sleep_tracker.html", context)

@login_required
def nutritionTracker(request):
    user = request.user
    account = Account.objects.get(username=user.username)
    context = {
        'account': account,
    }
    return render(request, "HealthTracker/user_page/tracker_pages/nutrition_tracker.html", context)

@login_required
def health_info(request):
    user = request.user
    user_instance = Account.objects.get(username = user.username)
    try:
        health_info = UserHealthInfo.objects.get(username=user_instance)
    except UserHealthInfo.DoesNotExist:
        health_info = None
    
    if request.method == 'POST':
        form = HealthInfoForm(request.POST, instance=health_info)
        if form.is_valid():
            health_data = form.save(commit=False)
            health_data.username = user_instance
            health_data.save()
            return redirect('index')  # Redirect to the same page after saving
    else:
        form = HealthInfoForm(instance=health_info)

    context = {
        'health_info': health_info,
        'form': form,
    }
    return render(request, 'HealthTracker/user_page/tracker_pages/health_info.html', context)
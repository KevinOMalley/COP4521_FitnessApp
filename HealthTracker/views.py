from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from django.template import loader
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from HealthTracker.models import Account, UserHealthInfo, MyAccountManager, WorkoutEntry, Nutrition, Sleep
from .forms import RegisterForm, AuthenticationForm, HealthInfoForm, RecordWorkoutForm, RecordSleepForm, \
    RecordNutritionForm


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
            return redirect('nutrition-tracker')
    else:
        form = HealthInfoForm(instance=health_info)

    context = {
        'health_info': health_info,
        'form': form,
    }
    return render(request, 'HealthTracker/user_page/tracker_pages/health_info.html', context)


@login_required
def record_workout(request):
    user = request.user
    try:
        user_instance = Account.objects.get(id=user.id)
    except Account.DoesNotExist:
        # Handle the case where the user doesn't exist
        return HttpResponse("User not found")

    if request.method == 'POST':
        form = RecordWorkoutForm(request.POST)
        if form.is_valid():
            workout_data = form.save(commit=False)
            workout_data.username = user_instance  # Associate the workout with the user
            workout_data.save()
            return redirect('workout-tracker')
    else:
        form = RecordWorkoutForm()

    context = {
        'form': form,
    }
    return render(request, 'HealthTracker/user_page/tracker_pages/record-workout.html', context)

@login_required
def record_sleep(request):
    user = request.user
    user_instance = Account.objects.get(id=user.id)
    if request.method == 'POST':
        form = RecordSleepForm(request.POST)
        if form.is_valid():
            sleep = form.save(commit=False)
            sleep.id = user_instance.id  # Associate the Sleep instance with the current user's id
            # sleep.total_sleep_duration = sleep.get_total_sleep_duration()
            print("Sleep instance created:", sleep)  # Debugging line
            sleep.save()
            print("Sleep instance saved:", sleep)  # Debugging line
            return redirect('sleep-tracker')
        else:
            print("Form is not valid:", form.errors)  # Debugging line
    else:
        form = RecordSleepForm()
    return render(request, 'HealthTracker/user_page/tracker_pages/record-sleep.html', {'form': form})

@login_required
def record_nutrition(request):
    user = request.user
    user_instance = Account.objects.get(id=user.id)
    if request.method == 'POST':
        form = RecordNutritionForm(request.POST)
        if form.is_valid():
            nutrition = form.save(commit=False)
            nutrition.user = user_instance  # Associate the Nutrition instance with the current user's id
            nutrition.save()
            return redirect('nutrition-tracker')
        else:
            print("Form is not valid:", form.errors)  # Debugging line
    else:
        form = RecordNutritionForm()
    return render(request, 'HealthTracker/user_page/tracker_pages/record-nutrition.html', {'form': form})


@login_required
def display_workout(request):
    user = request.user
    account = Account.objects.get(username=user.username)
    workouts = WorkoutEntry.objects.filter(id=account.id)
    context = {
       'workouts': workouts
    }
    return render(request, 'HealthTracker/user_page/tracker_pages/display-workout.html', context)

@login_required
def display_sleep(request):
    user = request.user
    user_instance = Account.objects.get(id=user.id)
    sleeps = Sleep.objects.filter(id=user_instance.id)  # Retrieve sleep records associated with the current user's id
    context = {
        'sleeps': sleeps
    }
    return render(request, 'HealthTracker/user_page/tracker_pages/display-sleep.html', context)

@login_required
def display_nutrition(request):
    user = request.user
    user_instance = Account.objects.get(id=user.id)
    nutritions = Nutrition.objects.filter(id=user_instance.id)
    return render(request, 'HealthTracker/user_page/tracker_pages/display-nutrition.html', {'nutritions': nutritions})
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.user_profile, name='profile'),
    path('health/', views.health_info, name='health'),
    path('user_home/', views.userHome, name='user_home'),
    path('workout-tracker/', views.workoutTracker, name='workout-tracker'),
    path('sleep-tracker/', views.sleepTracker, name='sleep-tracker'),
    path('nutrition-tracker/', views.nutritionTracker, name='nutrition-tracker'),
    path('record-workout', views.record_workout, name='record-workout'),
    path('record-food', views.record_food, name='record-food'),
    path('record-sleep', views.record_sleep, name='record-sleep'),
    path('display-workout', views.display_workout, name='display-workout'),
    path('display-sleep', views.display_sleep, name='display-sleep'),
    path('display-food', views.display_food, name='display-food'),
]

from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager



class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have email address")
        if not username:
            raise ValueError("Users must have a username")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username,password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
        

class Account(AbstractBaseUser):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="date joined", auto_now=True)

    #required fields for django user models
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    #custom
    is_child = models.BooleanField(default=False)
    is_adult = models.BooleanField(default=True)

    objects = MyAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
    
    
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True


class Userhealth(models.Model):
    username = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key = True,)
    weight = models.IntegerField()
    height = models.IntegerField()
    goals = models.TextField(null=True)


class FoodEntry(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=50)
    calories = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    meal_type = models.CharField(max_length=20, choices=[
        ('breakfast', 'Breakfast'),
        ('brunch', 'Brunch')
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack')
    ])
    
    '''
    User can add notes about the food they had. 
    -How they felt about it. More or less. Taste, etc.
    -Nutritional facts that they would like to keep track of based on different diets
    '''
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.food_name} - {self.calories} calories ({self.user.username}) - {self.meal_type}"
    
    
class Goals(models.Models):
    # Weight Goal
    # Step Goal
    # Calorie Goal
    # Sleep Goal
    pass
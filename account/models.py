from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, username, first_name, password=None):
        if not username:
            raise ValueError('Users must have a username')
        if not first_name:
            raise ValueError('Users must have a first name')

        user = self.model(
            username = username,
            first_name = first_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, password):
        user = self.create_user(
            username = username,
            password = password,
            first_name = first_name
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    username = models.CharField(verbose_name='username', max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30)
    total_revenue = models.DecimalField(max_digits=500, decimal_places=2, default=0)
    total_expenses = models.DecimalField(max_digits=500, decimal_places=2, default=0)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name']

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
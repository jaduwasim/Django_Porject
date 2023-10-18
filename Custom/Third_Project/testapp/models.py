from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self,email, phone, first_name, last_name, password=None, password2=None):
        if not phone:
            raise ValueError('Phone is Mandatory!! please Provide...')

        user = self.model(
            email = self.normalize_email(email),
            phone = phone,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, phone, first_name, last_name, password=None):
        user = self.create_user(
            email,
            phone=phone,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email Address', unique=True, max_length=255)
    phone = models.IntegerField(verbose_name='Mobile No.', unique=True)
    first_name = models.CharField(verbose_name='First Name' , max_length=255)
    last_name = models.CharField(verbose_name='Last Name' , max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    objects = MyUserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['email','first_name', 'last_name',]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_lable):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
    
    class Meta:
        db_table = 'User'
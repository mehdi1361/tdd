from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_field):
        """create and save new user"""
        if not email:
            raise ValueError("users must have email address")
            
        user = self.model(email=self.normalize_email(email), **extra_field)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password):
        """create super user"""
        user = self.create_user(email, password)
        user.is_staff =True
        user.is_superuser = True
        user.save(self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User model"""

    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'


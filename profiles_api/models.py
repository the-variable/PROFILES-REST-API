from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create new user profile"""
        if not email:
            raise ValueError('User must provide email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_spueruser(self, email, name, password):
        """Create and save new super user """
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = Trueuser.save(using=self._db)



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full nameof user"""
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        """Return string representation of user"""
        return self.email
    

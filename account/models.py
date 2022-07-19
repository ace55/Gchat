import email
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


'''
Overwriting the built in user creation

'''

class MyAcountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            return ValueError("Email Address is Required")
        if not username:
            return ValueError("Username is Required")
        # lower case the email input
        user = self.model(
            email = self.normalize_email(email),
            username= username, 
        )        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username= username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user




def get_profile_image_path(self, filename):
    return 'profile_images/' + str(self.pk) + '/profile_image.png'

def get_default_profile_image():
    return "hmbgc/default_profile.png"

class Account(AbstractBaseUser):

    email = models.EmailField(verbose_name='email' , max_length=60, unique= True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date_joined',auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.ImageField(max_length=255, upload_to =get_profile_image_path, null= True, blank = True, default= get_default_profile_image)
    hide_email= models.BooleanField(default=True)

    objects = MyAcountManager()

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS= ['username']


    def __str__(self):
        return self.username
    
    # set uploaded profile image to 'profile_image'
    def get_profileimage_filename(self):
        return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
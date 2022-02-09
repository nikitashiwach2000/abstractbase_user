# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# from django.utils import timezone
# from django.utils.translation import gettext_lazy as _ 
# from .manager import CustomUsermanager


# # Create your models here.
# class CustomUser(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique = True)
#     is_staff = models.BooleanField(default = True)
#     is_active = models.BooleanField(default = True)
#     is_superuser = models.BooleanField(default = True)
#     date_joined = models.DateTimeField(default = timezone.now)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELD = []
    
#     objects = CustomUsermanager()
#     def __str__(self):
#         return self.email
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    
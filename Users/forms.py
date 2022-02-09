# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import CustomUser

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ('email',)

    

# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = CustomUser
#         fields = ('email',)

#     # model = CustomUser
#     # fields =('email',)
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)

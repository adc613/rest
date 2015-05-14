from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, password, first_name='Jane', last_name='Doe'):
        if not email:
            raise ValueError('User must have email')

        if not password:
            raise ValueError('User must have password')

        user = self.model(
                email = self.normalize_email(email),
                first_name = first_name,
                last_name = last_name,
                )

        #Should be False but will leave it as True for now, because I don't
        #want to do email verifciation
        user.is_active = True
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, first_name="John",
            last_name="Doe"):
        user = self.create_user(email,password, first_name, last_name)
        user.is_active=True;
        user.is_superuser=True
        user.is_staff=True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    creation_date = models.DateTimeField(auto_now_add=True, editable=False)
    username = models.CharField(max_length=32)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=32) 
    last_name = models.CharField(max_length=32) 
    is_active = models.BooleanField(default=False)
    is_superuser = False
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def get_full_name():
        return self.first_name + ' ' + self.last_name

    def get_short_name():
        return self.first_name

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, phone, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an Email')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, phone, password=None):
    	user = self.create_user(username, email, phone, password=password)
    	user.is_staff = True
    	user.save(using=self._db)
    	return user


class CustomUser(AbstractBaseUser):
    username = models.CharField('Имя', max_length=50)
    email = models.EmailField('Почта', max_length=100, unique=True)
    phone = PhoneNumberField('Номер', unique=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']

    def has_perm(self, perm, obj=None):
    	return True

    def has_module_perms(self, app_label):
    	return True

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
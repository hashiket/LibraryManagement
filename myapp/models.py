import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin



class UserManager(BaseUserManager):
  
    def create_user(self, email, password=None):
        
        if not email:
            raise ValueError('Users Must Have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

    def get_full_name(self):
        pass

    def get_short_name(self):
        pass

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
       return self.is_admin

    def has_perm(self, perm, obj=None):
       return self.is_superuser

    def has_perm(self, perm, obj=None):
        user_perms = []
        if self.is_staff:
            groups = self.groups.all()
            for group in groups:
                perms = [(f"{x.content_type.app_label}.{x.codename}") for x in group.permissions.all()]
                user_perms += perms

 

            if perm in user_perms:
                return True
        return (self.is_admin or self.is_superuser)

 

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True
        
    @is_staff.setter
    def is_staff(self, value):
        self._is_staff = value


class CustomUser(AbstractBaseUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
        )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        
        db_table = "login"
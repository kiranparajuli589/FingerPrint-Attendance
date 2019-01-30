from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from PIL import Image



class UserManager(BaseUserManager):
    def create_user(self, email, fingercode=None, password=None):
        if not email:
            raise ValueError('User must have a unique email address!!!')

        user = self.model(email=self.normalize_email(email=email))
        user.fingercode = fingercode
        user.set_password(password)
        user.save()
        return user

    def create_staff_user(self, email, fingercode, password=None):
        user = self.create_user(email, fingercode, password=None)

        if not fingercode:
            raise ValueError('User must have a fingercode!!!')

        user.set_password(password)
        user.is_staff = True
        user.save()
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=None)

        user.set_password(password)
        user.is_staff = True
        user.is_admin = True
        user.save()
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=50, verbose_name='Email Address')
    full_name = models.CharField(max_length=100,null=True, blank=True, verbose_name='Full Name')
    fingercode = models.CharField(max_length=10,null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now(), verbose_name='Registered Date')

    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] #  Fingercode

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


class Profile(models.Model):
    ch = (                                  # choices for user group
        ('NPS', 'Nipuna Prabidhik Sewa'),
        ('PGM', 'Pokhara Green Mart')
    )
    designation_ch = (                                  # choices for user designation
        ('CEO', 'CEO'),
        ('PM', 'Project Manager'),
        ('HRM', 'Human Resource Manager'),
        ('Dev', 'Developer'),
        ('Intern', 'Internship')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, null=True, blank=True)
    phone = models.IntegerField(verbose_name='Phone Number', unique=True, null=True, blank=True)
    bio = models.TextField(verbose_name='Personal Detail', null=True, blank=True)
    group = models.CharField(max_length=3, choices=ch)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return '%s  Profile' % self.user.full_name

    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)

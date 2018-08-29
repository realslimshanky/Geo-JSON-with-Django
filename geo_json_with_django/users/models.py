# Third Party Stuff
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.postgres.fields import CIEmailField
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

# Geo JSON with Django Stuff
from geo_json_with_django.base.models import UUIDModel


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email: str, password: str, is_staff: bool,
                     is_superuser: bool, **extra_fields):
        """Creates and saves a User with the given email and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, is_staff=is_staff, is_active=True, is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email: str, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email: str, password: str, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class User(AbstractBaseUser, UUIDModel, PermissionsMixin):
    name = models.CharField(_('Full Name'), max_length=120)
    # https://docs.djangoproject.com/en/1.11/ref/contrib/postgres/fields/#citext-fields
    email = CIEmailField(_('email address'), unique=True, db_index=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    # Language choices as defined by ISO 639 https://en.wiktionary.org/wiki/Index:All_languages
    language = models.CharField(max_length=2, choices=(
        ('en', 'English'),
        ('fr', 'French'),
        ('de', 'German'),
        ('it', 'Italian'),
        ('ja', 'Japanese'),
        ('hi', 'Hindi'),
        ('ko', 'Korean'),
        ('ru', 'Russian')
    ))
    # Currency choices as defined by ISO 4217 https://en.wikipedia.org/wiki/ISO_4217#Active_codes
    currency = models.CharField(max_length=3, choices=(
        ('USD', 'United States dollar'),
        ('EUR', 'Euro'),
        ('JPY', 'Japanese yen'),
        ('INR', 'Indian rupee'),
        ('KPW', 'North Korean won'),
        ('KRW', 'South Korean won'),
        ('RUB', 'Russian ruble'),
    ))
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text='Designates whether the user can log into this admin site.')

    is_active = models.BooleanField('active', default=True,
                                    help_text='Designates whether this user should be treated as '
                                              'active. Unselect this instead of deleting accounts.')
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('-date_joined', )

    def __str__(self):
        return str(self.id)

    def get_name(self) -> str:
        """Returns the name of user.
        """
        return self.name

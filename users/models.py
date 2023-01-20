from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from django.core.validators import RegexValidator

ORDINARY_USER, MANAGER, SUPER_ADMIN = (
    'ordinary_user',
    'manager',
    'super_admin'
)

VIA_EMAIL,VIA_PHONE,VIA_USERNAME=(
    "via_email",
    "via_phone",
    "super_admin"
)

MALE,FEMALE=(
    "male",
    "femail"
)



class User(AbstractUser):
    _validate_phone=RegexValidator(
        regex=r"^9\d{12}$",
        message='Telefon raqamingiz 9 bilan boshlanib va 12 ta raqamdan iborat bolsin',
    )


    USER_ROLES=(
        (ORDINARY_USER, ORDINARY_USER),
        (MANAGER,MANAGER),
        (SUPER_ADMIN,SUPER_ADMIN)    
    )
    AUTH_TYPE_CHOICES=(
        (VIA_EMAIL,VIA_EMAIL),
        (VIA_PHONE,VIA_PHONE),
        (VIA_USERNAME,VIA_USERNAME),
    )
    SEX_CHOICES=(
        (MALE,MALE),
        (FEMALE,FEMALE)
    )

    

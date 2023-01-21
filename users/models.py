from datetime import datetime,timedelta #timedeltani vaqt qoshishda ishlatamiz
from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser,UserManager
from django.core.validators import RegexValidator
import random

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

PHONE_EXPIRE=2
EMAIL_EXPIRE=5

class UserConfirmation(models.Model):
    TYPE_CHOICES=(
        (VIA_PHONE, VIA_PHONE),
        (VIA_EMAIL, VIA_EMAIL)
    )

    code=models.CharField(max_length=4)
    user=models.ForeignKey('users.User',on_delete=models.CASCADE)
    verify_type=models.CharField(max_length=31, choices=TYPE_CHOICES)
    expiration_time=models.DataTimeField(null=True)
    is_confirmed=models.BooleanField(default=False)


    def __str__(self):
        return str(self.user.__str__())

    
    def save(self,*args,**kwargs):
        if not self.pk:
            if self.verify_type==VIA_EMAIL:
                self.expiration_time=datetime.now()+timedelta(minutes=EMAIL_EXPIRE)

            else:
                self.expiration_time=datetime.now()+timedelta(minutes=PHONE_EXPIRE)
            
        super(UserConfirmation, self).save(*args,**kwargs)




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
        (VIA_USERNAME,VIA_USERNAME)
    )
    SEX_CHOICES=(
        (MALE,MALE),
        (FEMALE,FEMALE)
    )

    
    user_roles=models.CharField(max_length=31,choices=USER_ROLES, default=ORDINARY_USER)
    auht_type=models.CharField(max_length=35, choices=AUTH_TYPE_CHOICES, default=VIA_USERNAME)
    sex=models.CharField(max_length=20, choices= SEX_CHOICES, null=True)
    email=models.EmailField(null=True,unique=True)
    phone_number=models.CharField(max_length=12,null=True, unique=True,validators=[_validate_phone])
    bio=models.CharField(max_length=200, null=True)

    
    object=UserManager()


    def __str__(self):
        return self.username

    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


    def create_verify_code(self,verify_type):
        code="".join([str(random.randint(0,100)%10) for _ in range(4)])
        UserConfirmation.objects.create(
            user_id=self.id,
            verify_type=verify_type,
            code=code
        )
        return code 


    


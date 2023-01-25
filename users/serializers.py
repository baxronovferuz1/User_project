from rest_framework import serializers
from users.models import User,UserConfirmation
from start_project.utility import check_email_or_phone
from users.models import VIA_EMAIL,VIA_PHONE
from rest_framework.exceptions import ValidationError


class SignUPSerializer(serializers.ModelSerializer):
    guid=serializers.UUIDField(read_only=True)



    def __init__(self, *args, **kwargs):
        super(SignUPSerializer,self).__init__(*args, **kwargs)
        self.fields['email_phone_number']=serializers.CharField(required=False)


    class Meta:
        model=User
        fields=(
            "guid",
            "auth_type",
            "auth_status"
        )

        extra_kwargs={
            "auth_type":{"read_only":True, "required":False},
            "auth_status":{'read_only':True, "required":False}
        }

    

    @staticmethod
    def auth_validate(in_data):
        user_input=str(in_data.get('email_phone_number'))
        input_type=check_email_or_phone(user_input)
        if input_type=="email":
            data={
                "email":in_data.get("email_phone_number"),
                "auth_type":VIA_EMAIL
            }

        elif input_type=="phone":
            data={
                "email":in_data.get("email_phone_number"),
                "auth_type":VIA_PHONE
            }

        elif input_type is None:
            data={
                'success':False,
                'message':"you must send email_adress or phone number"
             
            }
            raise ValidationError(data)
        
        else:
            data={
                'success':False,
                "message":"you must send email_adress or phone number"
            }
            raise ValidationError(data)
        return data
        
    

    def validate_email_phone_number(self,value):
        value=value.lower()


        if value and User.objects.filter(email=value).exists():
            data={
                "success":False,
                "message":"this email is already being used"
            }
            raise ValidationError(data)
        
        elif value and User.objects.filter(phone_number=value).exists():
            data={
                "success":False,
                "message":"this phone number is already being used"
            }
            raise ValidationError(data)

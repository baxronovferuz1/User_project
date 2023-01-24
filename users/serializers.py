from rest_framework import serializers
from users.models import User,UserConfirmation


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
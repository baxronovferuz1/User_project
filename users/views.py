from .serializers import SignUPSerializer
from rest_framework.generics import CreateAPIView
from rest_framework import permissions
from .models import User


class CreareUserview(CreateAPIView):
    model = User
    permission_classes=(permissions.AllowAny,)
    serializer_class=SignUPSerializer

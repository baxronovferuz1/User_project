from django.urls import path
from .views import CreareUserview

urlpatterns=[
    path("signup/",CreareUserview.as_view(), name='signup')
]
# app/users/views.py
from rest_framework import viewsets
from app.users.models import CustomUser
from app.users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

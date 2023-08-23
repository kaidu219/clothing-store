from django.contrib.auth import authenticate
from django.db.utils import IntegrityError

from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import status

from users.models import Favorite
from users.permissions import IsOwnerOrAdmin
from users.mixins import FavoriteMixins, UserDetailMixins
from users.serializers import (
    UserSerializer, LoginSerializer, FavoriteSerializer
)


class UserDetailView(UserDetailMixins):
    """
    Класс для отображения и изменения информации о текущем пользователе
    """
    permission_classes = [IsOwnerOrAdmin]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class RegisterAPIView(APIView):
    """
    Класс для регистрации пользователя
    """
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class LoginAPIView(APIView):
    """
    Класс для аутентификации пользователя,
    после успешной аутентификации генериуется токен
    """
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=400)

        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )

        if not user:
            return Response({'error': 'Invalid credentials'}, status=400)

        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


class FavoriteView(FavoriteMixins):
    """
    Класс для отображения избранных товаров, 
    пользователь может только добавлять, удалять и 
    детально просмотривать избранные товары
    """
    serializer_class = FavoriteSerializer
    permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

    def create(self, request):
        user = request.user
        serializer = FavoriteSerializer(
            data=request.data, context={'user': user})
        if serializer.is_valid():
            try:
                serializer.save()
            except IntegrityError:
                return Response({'error': 'Этот товар уже добавлен в избранное'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

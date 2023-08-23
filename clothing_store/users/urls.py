from rest_framework.routers import DefaultRouter

from django.urls import path
from users.views import (FavoriteView, LoginAPIView,
                         RegisterAPIView, UserDetailView)

router = DefaultRouter()

router.register(r'favorites', FavoriteView, basename='favorite')

urlpatterns = [
    path('users/detail/', UserDetailView.as_view(), name='user-detail'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('register/', RegisterAPIView.as_view(), name='register')
]

urlpatterns += router.urls

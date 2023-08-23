from rest_framework import viewsets, mixins
from rest_framework.generics import RetrieveUpdateDestroyAPIView


class FavoriteMixins(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    pass


class UserDetailMixins(RetrieveUpdateDestroyAPIView):
    pass

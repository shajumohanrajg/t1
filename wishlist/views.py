from django.shortcuts import render
from rest_framework import generics
from .serializers import UserWishlistSerializer
from rest_framework import permissions
from .models import UserWishlist
from rest_framework.response import Response
from rest_framework.views import APIView
from authentication.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication



class UserWishlistDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = UserWishlistSerializer

    def get_queryset(self):
        # Filter the wishlist items by the authenticated user
        return UserWishlist.objects.filter(wishlist_user=self.request.user)


# class UserWishlistList(generics.ListCreateAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     authentication_classes = [JWTAuthentication]
#     serializer_class = UserWishlistSerializer

#     def get_queryset(self):
#         # Return all wishlist items for the authenticated user
#         return UserWishlist.objects.filter(wishlist_user=self.request.user)

#     def perform_create(self, serializer):
#         # Automatically associate the wishlist with the logged-in user
#         serializer.save(wishlist_user=self.request.user)

class UserWishlistCreateAPIView(generics.ListCreateAPIView):
    serializer_class = UserWishlistSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]


    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def get_queryset(self):
        return UserWishlist.objects.filter(wishlist_user=self.request.user)
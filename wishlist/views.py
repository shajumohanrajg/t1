from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics, permissions
from .serializers import UserWishlistSerializer
from .models import UserWishlist


class UserWishlistDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = UserWishlistSerializer

    def get_queryset(self):
        # Filter the wishlist items by the authenticated user
        return UserWishlist.objects.filter(wishlist_user=self.request.user)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()  # Fetch the instance using the ID from the URL
        self.perform_destroy(instance)  # Delete the instance
        
        # Customize the response after deletion
        return Response({"detail": "Wishlist item deleted successfully."}, status=status.HTTP_204_NO_CONTENT)



class UserWishlistCreateAPIView(generics.ListCreateAPIView):
    serializer_class = UserWishlistSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return UserWishlist.objects.filter(wishlist_user=self.request.user)

    def perform_create(self, serializer):
        # Automatically associate the wishlist with the logged-in user
        serializer.save(wishlist_user=self.request.user)

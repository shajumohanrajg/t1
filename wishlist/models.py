from django.db import models
from authentication.models import User
from myweb.models import Registration


class UserWishlist(models.Model):
    wishlist_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlists')
    wishlist_registration = models.ForeignKey(Registration, on_delete=models.CASCADE, related_name='wishlists')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.wishlist_user.username}'s wishlist for {self.wishlist_registration}"
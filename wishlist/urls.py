from django.urls import path
from . import views


urlpatterns = [
    # path('wishlist/', views.WishlistAPIView.as_view(), name='wishlist'),
    # path('wishlist/<int:id>/', views.WishlistDetailAPIView.as_view(), name='wishlist-detail')
    # path('wishlists/<int:pk>/', views.UserWishlistView.as_view(), name='user_wishlist'),
    path('wishlists/', views.UserWishlistCreateAPIView.as_view(), name='user_wishlists'),
    path('wishlists/<int:pk>/', views.UserWishlistDetail.as_view(), name='user_wishlist'),
]

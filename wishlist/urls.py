# from django.urls import path
# from . import views
from django.urls import path
from .views import UserWishlistCreateAPIView, UserWishlistDetail


# urlpatterns = [
#     # path('wishlist/', views.WishlistAPIView.as_view(), name='wishlist'),
#     # path('wishlist/<int:id>/', views.WishlistDetailAPIView.as_view(), name='wishlist-detail')
#     # path('wishlists/<int:pk>/', views.UserWishlistView.as_view(), name='user_wishlist'),
#     path('wishlists/', views.UserWishlistCreateAPIView.as_view(), name='user_wishlists'),
#     path('wishlists/<int:pk>/', views.UserWishlistDetail.as_view(), name='user_wishlist'),
# ]

urlpatterns = [
    path('wishlists/', UserWishlistCreateAPIView.as_view(), name='wishlist-list-create'),
    path('wishlists/<int:pk>/', UserWishlistDetail.as_view(), name='wishlist-detail'),
]

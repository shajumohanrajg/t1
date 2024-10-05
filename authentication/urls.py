from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name="register"),
    path('email-verify/', views.VerifyEmail.as_view(), name="email-verify"),
    path('login/', views.LoginAPIView.as_view(), name="login"),
    # path('profile-data/', views.TestAuthenticationView.as_view(), name="profile"),
    path('request-reset-email/', views.RequestPasswordResetEmail.as_view(), name='request-reset-email'),
    path('password-reset/<uidb64>/<token>/', views.PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
    path('password-reset-complete/', views.SetNewPasswordAPIView.as_view(), name='password-reset-complete'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change-password'),
    # path('profiles/', views.UserProfileListCreateView.as_view(), name='userprofile-list'),
    # path('profiles/<int:pk>/', views.UserProfileDetailView.as_view(), name='userprofile-detail'),
    path('profiles/', views.UserProfileDetailView.as_view(), name='userprofile-detail'),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

from rest_framework import generics, status, views
from .serializers import (RegisterSerializer, EmailVerificationSerializer, LoginSerializer,
                          RestPasswordEmailRequestSerializer, SetNewPasswordSerializer, ChangePasswordSerializer,UserProfileSerializer)
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
import jwt
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
import logging
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import Util
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import Token
from rest_framework.generics import GenericAPIView
# from ..myweb.serializers import Registration


logger = logging.getLogger(__name__)


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        user_data = request.data
        serializer = self.serializer_class(data=user_data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        
        token = RefreshToken.for_user(user).access_token
        print("Token",token)
        # current_site = get_current_site(request).domain
        # print(current_site)
        current_site = "http://192.168.11.86:3000/"
        print("Current Site",current_site)

        relative_link = reverse('email-verify')

        # absurl = f'https://{current_site}{relative_link}?token={token}'
        absurl = request.build_absolute_uri(reverse('email-verify')) + f"?token={token}"


        email_body = f"Hi {user.username},\nUse link below to verify your email:\n {absurl}"
        data = {
            "to_email": user.email,
            "email_body": email_body,
            'email_subject': "verify Your email",
        }
        try:
            Util.send_email(data=data)

        except Exception as e:
            logger.error(f"Failed to send verification email to {user.email}:{e}")
            user.delete()
            return Response({"error": "Failed to send email"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(user_data, status=status.HTTP_201_CREATED)


class VerifyEmail(views.APIView):
    serializer_class = EmailVerificationSerializer
    # token_param_config = openapi.Parameter(
    #     'token', in_=openapi.IN_QUERY, description="Token for email verification", type=openapi.TYPE_STRING
    # )
    #
    # @swagger_auto_schema(manual_parameters=[token_param_config])

    def get(self, request):
        token = request.GET.get("token")

        if not token:
            return Response({"error":"Token is required"},status=status.HTTP_400_BAD_REQUEST)

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])

            user_id = payload.get('user_id')

            if not user_id:
                return Response({"error":"Invalid token payload: Missing user_id"},status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.get(id=user_id)

            if not user.is_verified:
                user.is_verified = True
                user.save()

            return Response({"email": "Successfully activated"}, status=status.HTTP_200_OK)

        except jwt.ExpiredSignatureError:
            return Response({"error": "Activation link expired"}, status=status.HTTP_400_BAD_REQUEST)

        except jwt.exceptions.DecodeError:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)

        except User.DoesNotExist:
            return Response({"error": "User Not found"}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({"error":f"An unexpected error occurred : {str(e)}"},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    # permission_classes = [JWTAuthentication]

    def post(self, request):
        serializer = self.serializer_class(data=request.data,
                                           context={"request":request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = RestPasswordEmailRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(request=request).domain

            relative_link = reverse('password-reset-confirm',
                                    kwargs={'uidb64': uidb64, 'token': token})
            abs_url = f'https://{current_site}{relative_link}'
            email_body = f"Hello, \n  Use Link below to reset your password:\n{abs_url}"
            data = {
                "email_body": email_body,
                'to_email': user.email,
                'email_subject': "Reset Your Password",
            }
            try:
                Util.send_email(data=data)
            except Exception as e:
                logger.error(f"Failed to send password reset email to {user.email}:{e}")
                return Response({"error": "Failed to send email"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"Success": "If an account with that email exists, We Have sent you a link a rest your password"}, status=status.HTTP_200_OK)


class PasswordTokenCheckAPI(generics.GenericAPIView):
    @staticmethod
    def get(uidb64, token):

        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({"error": "Token is not valid, please request a new one"},
                                status=status.HTTP_401_UNAUTHORIZED)

            return Response({"success": True, 'message': "Credentials valid", 'uidb64': uidb64,
                             'token': token}, status=status.HTTP_200_OK)

        except DjangoUnicodeDecodeError as e:
            logger.error(f"Decoding error during password reset token check: {e}")

            return Response({"error": "Token is not valid, please request a new one"},
                            status=status.HTTP_401_UNAUTHORIZED)


class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)
        return Response({"success": True, 'message': 'Password reset successfully'},
                        status=status.HTTP_200_OK)

# ?????????????
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.update(instance=request.user, validated_data=serializer.validated_data)
            return Response({"message": "Password updated successfully "}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class UserProfileListCreateView(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserProfileSerializer

class UserProfileDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

# class TestAuthenticationView(GenericAPIView):
#     permission_classes = [IsAuthenticated,]
#     # authentication_classes = [IsAuthenticated]

#     def get(self, request):
#         data = {
#             "msg":"its works mani"
#         }
#         return Response(data,status=status.HTTP_200_OK)
    
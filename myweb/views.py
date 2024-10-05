# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import generics
from .serializers import RegistrationSerializer, RegistrationSearchSerializer
from .models import Registration
from rest_framework import permissions
from rest_framework import generics
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import Token
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication


# RegistrationallList 



class RegistrationDetailsAPIView(generics.ListCreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        return Registration.objects.filter(user_id=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
        
# class RegistrationDetailsAPIView(generics.ListCreateAPIView):
#     serializer_class = RegistrationSerializer
#     queryset = Registration.objects.all()
#     permission_classes = (permissions.IsAuthenticated,)
#     authentication_classes = [JWTAuthentication]
   

#     def perform_create(self, serializer):
#         return serializer.save(user_id=self.request.user)

#     def get_queryset(self):
#         return self.queryset.filter(user_id=self.request.user)

class RegistrationGetIdAPIView(generics.RetrieveAPIView):
    serializer_class = RegistrationSerializer
    queryset = Registration.objects.all()
    # permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'user_id'


# class ViewOrNotNView(generics.RetrieveAPIView):
#     serializer_class = RegistrationSerializer
#     queryset = Registration.objects.all()
#     permission_classes = [permissions.IsAuthenticated]
#     lookup_field = 'user_id'




# class RegistrationGetIdAPIView(generics.RetrieveAPIView):
#     serializer_class = RegistrationSerializer
#     queryset = Registration.objects.all()
#     permission_classes = (permissions.IsAuthenticated,)


    # authentication_classes = [JWTAuthentication]
   

    # def perform_create(self, serializer):
    #     return serializer.save(user_id=self.request.user)

    # def get_queryset(self):
    #     return self.queryset.filter(user_id=self.request.user)


# class RegistrationEditAPIView(generics.RetrieveUpdateAPIView):
#     serializer_class = RegistrationSerializer
#     queryset = Registration.objects.all()
#     # permission_classes = (permissions.IsAuthenticated,)
#     # authentication_classes = [JWTAuthentication]
#     lookup_field = "id"

#     def get_object(self):
#         # Return the Registration object for the currently authenticated user
#         return Registration.objects.get(user_id=self.request.user)



class RegistrationEditAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        try:
            return Registration.objects.get(user_id=self.request.user)
        except Registration.DoesNotExist:
            raise NotFound("Registration not found for this user.")

    def perform_update(self, serializer):
        serializer.save(user_id=self.request.user)

class RegistrationSearchAPIView(generics.ListAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSearchSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    # authentication_classes = [JWTAuthentication]
    
    
    print(queryset)
    def get_queryset(self):
        queryset = super().get_queryset()
      
        user_id = self.request.query_params.get('user_id')
        date_of_birth = self.request.query_params.get('date_of_birth')
        gender = self.request.query_params.get('gender')
        mother_tongue = self.request.query_params.get('mother_tongue')
        caste = self.request.query_params.get('caste')
        religious = self.request.query_params.get('religious')
        state = self.request.query_params.get('state')
        district = self.request.query_params.get('district')
        marital_status = self.request.query_params.get('marital_status')
        print(date_of_birth)
        if user_id:
            queryset = queryset.filter(user_id = user_id)
        if gender:
            queryset = queryset.filter(gender__iexact=gender)
        if mother_tongue:
            queryset = queryset.filter(mother_tongue__iexact=mother_tongue)
        if caste:
            queryset = queryset.filter(caste__iexact=caste)
        if religious:
            queryset = queryset.filter(religious__iexact=religious)
        if state:
            queryset = queryset.filter(state__iexact=state)
        if district:
            queryset = queryset.filter(district__iexact=district)
        if marital_status:
            queryset = queryset.filter(marital_status__iexact=marital_status)

        # print("filter data :",queryset)
        return queryset

    # def get(self, request):
    #     query_set = self.get_queryset()
    #     serializer = RegistrationSearchSerializer(query_set, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)



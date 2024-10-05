from rest_framework import serializers
from .models import Registration
from authentication.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user_id.username")
    class Meta:
        model = Registration
        fields = '__all__'
        
        extra_fields = ['username']
        read_only_fields = ['user_id']


class RegistrationSearchSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user_id.username")
    class Meta:
        model = Registration
        fields = ['user_id','username', 'gender', 'height', 'weight', "date_of_birth",
                  'religious', 'caste', 'mother_tongue', 'photo1',
                  'educational_qualification','state','district','marital_status','job']

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Register


class RegisterTests(TestCase):
    def test_user_registration(self):
        url = reverse('user-register')
        data = {
            "name":'Test User',
            'email':'test@explample.com',
            'phone':'+911234567890',
            'password':'test123',
            'i_agree':True

        }

        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        

        reg = Register.objects.get(email="test@explample.com")
        self.assertEqual(reg.name,"Test User")
        self.assertEqual(reg.phone,"+911234567890")
    
    def test_invalid_user_registration(self):
        url = reverse('user-register')
        data = {
            "name":'Test User',
            'email':'test_Email',
            'phone':'1234567890',
            'password':'test123',
            'i_agree':True

        }

        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST) 
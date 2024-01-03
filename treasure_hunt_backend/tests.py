from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
# from .models import #etc

class UserTests(APITestCase):
    #TESTS ARE RUN ALPHABETICALLY AND MUST START WITH test
    def test_any_test(self):
        print("any_test")
        url = reverse("create-user")
        data = {"username": "electircboogaloo", "password": "ahh"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {"id": 1,"username": "electircboogaloo", "password": "ahh"})
        
    def test_create_user(self):
        print("test_create_user")
        url = reverse("create-user")
        data = {"username": "testeronee", "password": "stopLookingAtMyPassword"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, "testeronee")
        
    def test_missing_input_data(self):
        print("missing_input_data")
        url = reverse("create-user")
        data = {"undername": "uhOh", "passwrd": "NOtGood"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)
        
    def test_user_already_exists(self):
        print("test_user_already_exists")
        url = reverse("create-user")
        data = {"username": "twins", "password": "weAreTwinning"}
        data2 = {"username": "twins", "password": "howFun"}
        self.client.post(url, data)
        response = self.client.post(url, data2)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
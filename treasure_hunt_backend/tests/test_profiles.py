from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from ..models import Profile

# Profiles Endpoint
## Get a list of all profiles 
## Get a single profile 
## Posts a new profile when a user is created 
## Patch a new avatar 
## Patch newly found treasure 
## Patching the collection keeps previous treasures
## Deletes a profile when the related user is deleted
## Erroneous tests too (: 
###TESTS ARE RUN ALPHABETICALLY AND MUST START WITH test

class GetProfiles(APITestCase):
    def test_a_get_single_profile(self):
        urlu= reverse("user-list")
        data={"username": 'created-user-2',"password":'admin'}
        self.client.post(urlu,data)
        urlp=reverse('profile-detail',kwargs={'pk':1})
        response= self.client.get(urlp)   
        #print(response.data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data,{"id": 1,"user": 1, "avatar":"http://testserver/default.jpg", "treasures":[]})

    def test_b_get_all_profiles(self):
        urlu= reverse("user-list")
        data={"username": 'created-user',"password":'admin'}
        data2 ={"username": 'created-user-2',"password":'admin'}
        self.client.post(urlu,data)
        self.client.post(urlu,data2)
        urlp= reverse("profile-list")
        response= self.client.get(urlp)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data,[{"id": 2, "user": 2, "avatar": "http://testserver/default.jpg", "treasures": []},{"id": 3, "user": 3, "avatar": "http://testserver/default.jpg", "treasures": []}])
    
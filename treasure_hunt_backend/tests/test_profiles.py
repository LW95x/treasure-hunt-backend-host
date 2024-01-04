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

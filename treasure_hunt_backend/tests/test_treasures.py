from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from ..models import Treasure

# Treasures Endpoint
## Get a list of all available treasures 
## Get details of a specific treasure 
## Post a new treasure 
## Patch treasure details (admin only?) 
## Delete treasure (admin only?)
## Erroneous tests too (: 
###TESTS ARE RUN ALPHABETICALLY AND MUST START WITH test
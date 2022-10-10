from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status

# class AccountTests(APITestCase):

#     def test_create_account(self):
#         response = self.client.get('/getAll/')
#         print(response)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data,[])
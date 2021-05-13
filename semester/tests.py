from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate

from semester.models import Semester


class SemesterTests(TestCase):
    def setUp(self):
        self.semester = Semester.objects.create(semester='5', details='Just another semester')

    
    def test_get_all_semester(self):
        response = self.client.get('/sem/semester/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):
    def test_create_user_with_email_successful(self):
        """test create user with email successful"""
        email = "mhd.mosavi@gmail.com"
        password = "13610522"

        user = get_user_model().objects.create_user (
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        """Test email for a new user normalize"""
        email = "mhd.mosavi@GMAIL.COM"

        user = get_user_model().objects.create_user(email, "test1234")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test creating with no email raise error"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")


    def test_create_new_super_user(self):
        """test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            "test@gmail.com",
            "test123"
        )
        
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
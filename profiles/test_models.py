""" Tests for the Profiles apps models """
from django.shortcuts import get_object_or_404
from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile


class TestUserProfileModel(TestCase):
    """ Tests the UserProfile model """

    def test_profile_str(self):
        """Test UserProfile string method"""
        User.objects.create(username = 'newusertester')
        user = get_object_or_404(User, username="newusertester")
        user_profile = get_object_or_404(UserProfile, user=user)
        self.assertEqual(str(user.username), "newusertester")

    def test_profile_user_name(self):
        """Test UserProfile user_name method"""
        User.objects.create(username = 'newusertester')
        user = get_object_or_404(User, username="newusertester")
        user_profile = get_object_or_404(UserProfile, user=user)
        self.assertEqual(user_profile.user.username, "newusertester")

    def test_create_user_profile_receiver(self):
        """Test UserProfile create receiver"""
        # Create new standard user
        newuser = User.objects.create_user(
            'testuser2', 'testuser2@test.com', 'testuser2password')
        user_profile = get_object_or_404(UserProfile, user=newuser)
        # Test new user user_name
        self.assertTrue(user_profile)
        self.assertEqual(user_profile.user.username, "testuser2")

    def test_update_user_profile_receiver(self):
        """Test UserProfile update receiver"""
        User.objects.create(username = 'newusertester')
        # Get standard user
        user = get_object_or_404(User, username="newusertester")
        # Update username
        user.username = "testuserupdated"
        user.save()
        user_profile = get_object_or_404(UserProfile, user=user)
        # Test updated user user_name
        self.assertTrue(user_profile)
        self.assertEqual(user_profile.user.username, "testuserupdated")

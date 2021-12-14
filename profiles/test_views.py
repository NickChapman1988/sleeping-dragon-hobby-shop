""" Test profiles app views """
from django.shortcuts import get_object_or_404
from django.test import TestCase
from django.urls import resolve
from django.contrib.auth.models import User
from checkout.models import Order
from .models import UserProfile



class TestProfileViews(TestCase):
    """ Tests for Profile views """

    def test_profile(self):
        """ Test resolving profile view """
        # Create test user
        User.objects.create_user(
            'unittestuser', 'unittestuser@test.com', 'unittestuserpassword')
        loginresponse = self.client.login(
            username='unittestuser', password='unittestuserpassword')
        self.assertTrue(loginresponse)
        found = resolve('/profile/')
        self.assertEqual(found.url_name, "profile")

    def test_order_history(self):
        """ Test resolving order history view """
        # Create test user
        User.objects.create_user(
            'unittestuser', 'unittestuser@test.com', 'unittestuserpassword')
        # login as test user
        loginresponse = self.client.login(
            username='unittestuser', password='unittestuserpassword')
        self.assertTrue(loginresponse)
        # Get user object
        user = get_object_or_404(User, username="unittestuser")
        # Get user profile object
        user_profile = get_object_or_404(UserProfile, user=user)
        # Create user order
        Order.objects.create(
            user_profile = user_profile,
            full_name = 'test user',
            email = 'test@test.com',
            phone_number = '0123456789',
            country = 'GB',
            town_or_city = 'test',
            street_address1 = 'test',
            order_total  = 15.00,
            delivery_cost = 2.00,
            grand_total = 17.00,
            stripe_pid = "Test Stripe PID",
        )
        # Get order object
        order = Order.objects.get(user_profile=user_profile)
        found = resolve(f'/profile/order_history/{order.order_number}')
        self.assertEqual(found.url_name, "order_history")

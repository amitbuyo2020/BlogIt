from django.test import TestCase
from django.contrib.auth import get_user_model

class UsersManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='normaluser@gmail.com', password='@mit_1999')

        self.assertEqual(user.email, 'normaluser@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass

        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='normaluser@gmail.com', password='@mit_1999')

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser('testuser2021python@gmail.com', password='@mit_19999')
        self.assertEqual(admin_user.email, 'testuser2021python@gmail.com')
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

        try:
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass

        with self.assertRaises(ValueError):
            User.objects.create_superuser(email='amitbuyo2021@gmail.com', password='@mit_19999', is_superuser=False)

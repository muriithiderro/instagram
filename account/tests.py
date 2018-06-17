from django.test import TestCase
from .models import Profile
from django.contrib.auth import get_user_model


class TestUserAndProfile(TestCase):
    

    def setUp(self):
        self.User = get_user_model()
        self.User.objects.create(username="admin", password="123")
    
    def tearDown(self):
        pass

    def test_the_user_instance(self):
        """
        This method checks
        """
        self.useradmin = self.User.objects.filter(username="admin").values_list('username',flat=True)[0]
        self.assertEquals(self.useradmin, 'admin')

    def test_post_save_signal_on_profile(self):
        pass
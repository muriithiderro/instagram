from django.test import TestCase
from .models import Photo,Comment
from django.contrib.auth import get_user_model
from .views import dashboard
from django.core.urlresolvers import reverse
from django.urls import resolve
# from django.contrib.auth.models import User

class TestPhotoAndUserAndCommentMethods(TestCase):
    def setUp(self):
        self.User = get_user_model()
        self.user_admin = self.User.objects.create(username='admin', password="123")
        self.test_image = Photo(user=self.user_admin, title="cool day", description="so cool")
        self.test_comment = Comment(photo=self.test_image, name=self.user_admin, body="nyce comment")
        self.test_image.save()
        

    def tearDown(self):
        pass

    def test_correct_instantiation_of_Photo_model(self):
        self.assertEquals(self.user_admin.username, 'admin')
        self.assertEquals(self.user_admin.password, '123')

        self.assertEquals(self.test_image.user, self.user_admin)
        self.assertEquals(self.test_image.title, 'cool day')
        self.assertEquals(self.test_image.description, 'so cool')

    def test_save_method_sluggifies_the_slug_field(self):
        self.test_image.save()
        self.assertEquals(self.test_image.slug, 'cool-day')
    
    def test_search_method_using_the_Q_function(self):
        self.query="o"
        photos = Photo.search(self.query)
        self.assertTrue(photos)

    def test_search_casing(self):
        self.query="O"
        photos = Photo.search(self.query)
        self.assertTrue(photos)

    def test_search_for_none_values(self):
        self.query="jfni3243SE/fjke"
        photos = Photo.search(self.query)
        self.assertFalse(photos)

    def test_comments_instantiation(self):
        self.assertEquals(self.test_comment.photo, self.test_image)
        self.assertEquals(self.test_comment.name, self.user_admin)
        self.assertEquals(self.test_comment.body, "nyce comment")



class DashboardTests(TestCase):
    def setUp(self):
        self.url = reverse('dashboard')
        self.response = self.client.get(self.url)
    def tearDown(self):
        pass

    def test_dashboard_status_code(self):
        self.assertEquals(self.response.status_code,200)

    def test_dashboard_url_resolves_dashboard_view(self):
        view = resolve('/')
        self.assertEquals(view.func, dashboard)




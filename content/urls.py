from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.dashboard, name="dashboard"),
    url(r'^post$',views.add_photo, name="add_photo"),
    # url(r'^comment/$', views.comment, name='comment')
]
from django.conf.urls import url

from django.contrib.auth.views import login
#With django 1.10 I need to pass the callable instead of 
#url(r'^login/$', 'django.contrib.auth.views.login', name='login')

from django.contrib.auth.views import logout
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.views import password_change
from django.contrib.auth.views import password_change_done
from django.contrib.auth.views import password_reset
from django.contrib.auth.views import password_reset_done
from django.contrib.auth.views import password_reset_confirm
from django.contrib.auth.views import password_reset_complete
from . import views

urlpatterns = [
        url(r'^login/$', login, name='login'),
        url(r'^logout/$', logout,{ 'template_name': 'registration/logout.html',}, name='logout'),
        url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),
        url(r'^password-change/$', password_change,{'template_name': 'registration/password_change_form.html',}, name='password_change'),
        url(r'^password-change/done/$', password_change_done, name='password_change_done'),
        url(r'^password-reset/$',password_reset,name='password_reset'),
        url(r'^password-reset/done/$',password_reset_done,name='password_reset_done'),
        url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',password_reset_confirm,name='password_reset_confirm'),
        url(r'^password-reset/complete/$',password_reset_complete,name='password_reset_complete'),
        url(r'^edit/$', views.edit, name='edit'),
        url(r'^register/$', views.register, name='register'),
        url(r'^profile/$', views.profile, name='profile'),

        ]



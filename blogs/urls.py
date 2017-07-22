from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<blogID>[0-9]*)/post/', views.write, name='write'),
    url(r'^(?P<blogID>[0-9]*)/posts/', views.see, name='see'),
    url(r'^(?P<blogID>[0-9]*)/comment/', views.comment, name='comment'),
]
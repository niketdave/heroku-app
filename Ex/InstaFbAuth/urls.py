
from django.conf import settings
from django.conf.urls import url
from . import views as facebookinsta_view

urlpatterns = [
    #url(r'^facebook$',facebookinsta_view.FacebookWebHookView),
    url(r'^instagram$',facebookinsta_view.InstagramWebHookView),
]

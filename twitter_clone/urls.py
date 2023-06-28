from django.contrib import admin
from django.urls import path
from tweet_app import views as tweet_app_views
from login import views as login_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", tweet_app_views.home, name="home"),
    path("success/", login_views.success_page, name="success_page"),
    path("registration/", login_views.registration_view, name="registration_view"),
    path("login/", login_views.login_view, name="login_view"),
    path("tweet/", tweet_app_views.tweet, name="tweet_view"),
]

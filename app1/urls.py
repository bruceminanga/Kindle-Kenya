# testing donations feature
from django.urls import path, include
from app1 import views
from .views import (
    home,
    aboutus,
    NewsletterSubscribeView,
)


app_name = "app1"

urlpatterns = [
    path("", views.home, name="home"),
    path("about-us/", views.aboutus, name="about-us"),
    path(
        "newsletter/subscribe/",
        NewsletterSubscribeView.as_view(),
        name="newsletter_subscribe",
    ),
    # donation feature
    path("donate/", views.donation_view, name="donation"),
    path("donate/process/", views.process_donation, name="process_donation"),
    path("submit-partnership/", views.submit_partnership, name="submit_partnership"),
]

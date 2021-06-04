from django.urls import path
from backend import views
from django.conf import settings

app_name = "backend"

urlpatterns = [
    path(
        "elections/",
        views.ElectionListView.as_view(),
        name="election-list",
    ),
    path("ballots/", views.BallotSubmitView.as_view(), name="ballot-submit"),
]

if not settings.CONNECT_TO_UOFT:
    urlpatterns.append(
        path(
            "bypasscookie/", views.BypassUofTCookieView.as_view(), name="bypass-cookie"
        )
    )

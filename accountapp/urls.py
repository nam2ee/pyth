from django.urls import path

from accountapp import views
from accountapp.views import hello_world

appname = "accountapp"

urlpatterns = [
    path('hello_world/',hello_world),
]

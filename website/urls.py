from django.urls import path

from . import views
from .views import HomeView, AboutView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('About', AboutView.as_view(), name='about'),
    path('Contact', ContactView.as_view(), name='contact'),
]

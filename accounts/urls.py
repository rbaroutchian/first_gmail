from django.urls import path
from .views import signin_view, signup_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('signin/', signin_view, name='signin'),


]

from django.urls import path
from .views import EmailCreateView, EmailListView, InboxView

urlpatterns = [
    path('create-email/', EmailCreateView.as_view(), name='create-email'),
    path('emails/', EmailListView.as_view(), name='email_list'),
    path('inbox/', InboxView.as_view(), name='inbox'),

]
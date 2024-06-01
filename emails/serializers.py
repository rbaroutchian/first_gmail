from rest_framework import serializers
from .models import Email, Inbox


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'


class InboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inbox
        fields = ['id', 'user', 'emails', 'subject_objects', 'body_objects']

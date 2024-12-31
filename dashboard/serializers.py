from rest_framework import serializers
from .models import Notification

class ChatRequestSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=1000)

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'user', 'title', 'message', 'is_read', 'created_at']
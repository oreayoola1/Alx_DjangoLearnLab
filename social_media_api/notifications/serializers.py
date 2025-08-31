from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.ReadOnlyField(source="actor.username")
    recipient = serializers.ReadOnlyField(source="recipient.username")
    target = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = ["id", "recipient", "actor", "verb", "target", "read", "timestamp"]

    def get_target(self, obj):
        if obj.target is None:
            return None
        # return a simple representation
        return {
            "type": obj.target_content_type.model,
            "id": obj.target_object_id,
            "repr": str(obj.target)
        }

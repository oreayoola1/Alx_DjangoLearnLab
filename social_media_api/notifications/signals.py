from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.contenttypes.models import ContentType
from accounts.models import CustomUser
from posts.models import Comment
from notifications.models import Notification

@receiver(post_save, sender=Comment)
def comment_notification(sender, instance, created, **kwargs):
    if not created:
        return
    post = instance.post
    if post.author != instance.author:
        Notification.objects.create(
            recipient=post.author,
            actor=instance.author,
            verb="commented",
            target_content_type=ContentType.objects.get_for_model(post),
            target_object_id=post.id
        )

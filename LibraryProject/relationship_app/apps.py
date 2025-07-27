from django.apps import AppConfig


class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'
<<<<<<< HEAD
def ready(self):
    import relationship_app.signals
=======
>>>>>>> e7580ffb8bc426a3eadaf316d6db45b07b6cb357

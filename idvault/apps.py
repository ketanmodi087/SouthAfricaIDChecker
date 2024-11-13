from django.apps import AppConfig

class IdvaultConfig(AppConfig):
    """
    Configuration class for the 'idvault' Django application.

    This class defines the configuration settings for the 'idvault' app,
    including specifying the default auto field type for model primary keys 
    and the name of the app.

    Attributes:
        default_auto_field (str): Specifies the type of auto-generated primary key field to use for models.
        name (str): The name of the application, used by Django to identify it.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "idvault"

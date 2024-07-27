from django.apps import AppConfig


class UserManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'User_Management'


class YourAppConfig(AppConfig):
    name = 'User_Management'

    def ready(self):
        import User_Management.signals


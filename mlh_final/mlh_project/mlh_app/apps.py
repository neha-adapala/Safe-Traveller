from django.apps import AppConfig


class MLHAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mlh_app'

    def ready(self):
        import mlh_app.signals

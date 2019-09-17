from django.apps import AppConfig


class EntityConfig(AppConfig):
    name = 'entity'

    def ready(self):
        import entity.signals  # noqa

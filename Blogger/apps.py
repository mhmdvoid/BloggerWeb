from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'Blogger'
    def ready(self):
        import Blogger.signals
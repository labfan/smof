from django.apps import AppConfig


class ActorsConfig(AppConfig):
    name = 'actors'

    def ready(self):
        super(ActorsConfig, self).ready()
        # noinspection PyUnresolvedReferences
        import actors.signals

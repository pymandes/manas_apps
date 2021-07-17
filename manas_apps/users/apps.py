from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "manas_apps.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import manas_apps.users.signals  # noqa F401
        except ImportError:
            pass

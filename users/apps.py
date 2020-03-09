from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # there is a conflict with the ready function
    #
    # def ready(self):
    #     import users.signals

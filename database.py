from django.db import IntegrityError

from tradeboard.models import *


class APIWrapperDB:
    @staticmethod
    def add_user(username, password):
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()

            return User.objects.get(
                username=username), "User successfully created"  # Возвращаем флаг успеха и сообщение
        except IntegrityError:
            return False, "User already exist"  # Возвращаем флаг неудачи и сообщение

    @staticmethod
    def check_user(username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return 'No such user. Please register first.'

from django.db import IntegrityError

from tradeboard.models import *


class APIWrapperDB:
    @staticmethod
    def add_user(username, password):
        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()

            return User.objects.get(
                username=username), "Пользователь успешно создан"  # Возвращаем флаг успеха и сообщение
        except IntegrityError:
            return False, "Уже есть пользователь с таким username"  # Возвращаем флаг неудачи и сообщение

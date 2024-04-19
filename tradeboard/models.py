from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def __str__(self):
        return {self.username}

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"

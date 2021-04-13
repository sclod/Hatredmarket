from django.db import models


class UserEmail(models.Model):
    #
    email = models.CharField(max_length=100,)

    def __str__(self) -> str:
        return str(self.email)


class Feedback(models.Model):
    #
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=1024)
    user_email = models.CharField(max_length=100)

    def __str__(self) -> str:
        return str(self.subject)

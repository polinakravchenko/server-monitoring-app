from django.db import models

class Servers(models.Model):
    server_name = models.CharField(max_length=55)
    time_notification = models.DateTimeField()
    type_notification = models.TextChoices("push","email")
    email_address = models.EmailField(max_length=254)
    server_group = models.TextChoices("general", "computing")
    type_server_group = models.TextChoices("m7g.medium", "c7g.medium")
    server_localization = models.CharField(max_length=50)

def __str__(self):
    return f"{self.server_name} {self.time_notification}"

class LoginMembers(models.Model):
    user_name = models.CharField(max_length=30)
    e_mail = models.EmailField()
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.user_name
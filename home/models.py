from django.db import models

class UserSimple(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.email}"

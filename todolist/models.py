from django.conf import settings
from django.db import models

class Task(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.deletion.CASCADE,
        blank=True,
        null=True,
    )
    date = models.DateField(
        auto_now = True
    )
    title = models.CharField(
        max_length = 100
    )
    description = models.TextField()
    is_finished = models.BooleanField(default = False)
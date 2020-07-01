from django.db import models


class ListItem(models.Model):
    content = models.TextField()
    is_done = models.BooleanField(default=False)


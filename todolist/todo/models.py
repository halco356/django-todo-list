from django.db import models


class ListItem(models.Model):
    content = models.TextField()


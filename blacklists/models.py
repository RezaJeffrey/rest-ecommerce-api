from django.db import models


class Blacklist(models.Model):
    name = models.CharField(max_length=255, blank=False, null=True)

    def __str__(self):
        return str(self.name)

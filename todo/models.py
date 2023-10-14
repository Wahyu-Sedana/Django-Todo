from django.db import models


class Todo(models.Model):
    title = models.TextField(max_length=200)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
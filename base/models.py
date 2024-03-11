from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length = 200)
    is_done = models.BooleanField(default = False)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

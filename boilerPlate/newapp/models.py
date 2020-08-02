from django.db import models

# Create your models here.
class TemporaryModel(models.Model):
    label = models.CharField(max_length = 200)
    text = models.TextField()

    def getText(self):
        return self.text[:200]

    def __str__(self):
        return self.label

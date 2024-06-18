from django.db import models

class Submit(models.Model):
    text = models.CharField(max_length=200)
    rating = models.FloatField()
    time = models.DateTimeField("date published")
    def __str__(self):
        return self.text

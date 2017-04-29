from django.db import models


class Picture(models.Model):
    feature = models.ImageField(upload_to="raw/")
    label = models.CharField(max_length=240)
    score = models.IntegerField()
    co2 = models.FloatField()
    recyclable = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

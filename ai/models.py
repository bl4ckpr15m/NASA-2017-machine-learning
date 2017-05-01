from django.db import models


class Picture(models.Model):
    feature = models.ImageField(upload_to="raw/")
    label = models.CharField(max_length=240, blank=True, null=True)
    score = models.IntegerField(default=0)
    co2 = models.FloatField(blank=True, null=True)
    recyclable = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.feature.path

    def __unicode__(self):
        return unicode(self.feature.path)

    class Meta:
        ordering = ('-created_at',)

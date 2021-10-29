from django.db import models

class Seminar(models.Model):
    name = models.TextField()
    location = models.TextField()
    dates = models.ManyToManyField("Date", blank=True)

    def __str__(self):
        return f"{self.name, self.location}"

class Date(models.Model):
    datum = models.DateField(null=True)
    starttime = models.TimeField(null=True)
    endtime = models.TimeField(null=True)

    def __str__(self):
        return f"{self.datum, self.starttime, self.endtime}"

    

from django.db import models

# Create your models here.
class List(models.Model):
    item = models.CharField(max_length= 1023)
    # completed = models.BooleanField(default=False)
    # heading = models.CharField(max_length = 32)

    def __str__(self):
        return self.item 
        # + ' | ' + self.heading

    objects = models.Manager
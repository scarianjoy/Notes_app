from django.db import models

# Create your models here.
class List(models.Model):
    item = models.CharField(max_length= 1023)
    completed = models.BooleanField(default=False)
    title = models.CharField(max_length = 32, default= 'No Title')

    def __str__(self):
        return self.item + ' | ' + str(self.completed) + ' | ' + self.title

    objects = models.Manager
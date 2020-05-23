from django.db import models


# Create your models here.
class Coordinate(models.Model):
    sequence = models.IntegerField()
    coordinate_x = models.IntegerField()
    coordinate_y = models.IntegerField()
    clicks = models.IntegerField()
    interval = models.IntegerField()


    # def __str__(self):
    #     return 'coordinate:'+self.coordinate_x, 'coordinate:'+self.coordinate_y

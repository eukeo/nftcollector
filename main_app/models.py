from django.db import models

class NFT(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=100)
    traits = models.CharField(max_length=100)
    number = models.IntegerField()

    def __str__(self):
        return self.name
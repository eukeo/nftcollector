from django.db import models
from django.urls import reverse

class NFT(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=100)
    traits = models.CharField(max_length=100)
    number = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'nft_id': self.id})
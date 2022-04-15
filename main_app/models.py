from django.db import models
from django.urls import reverse

CRYPTOS = (
    ('B', 'Bitcoin'),
    ('E', 'Etherium'),
    ('S', 'Solana')
)

class NFT(models.Model):
    name = models.CharField(max_length=50)
    breed = models.CharField(max_length=100)
    traits = models.CharField(max_length=100)
    number = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'nft_id': self.id})

class Listing(models.Model):
    market = models.CharField(max_length=15)
    crypto = models.CharField(
        max_length=1, 
            choices=CRYPTOS, 
            default=CRYPTOS[0][0]
    )

    nft = models.ForeignKey(NFT, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_crypto_display()} on {self.market}"

    class Meta:
        ordering = ['-market']
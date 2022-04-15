from django.contrib import admin
# Register your models here.
from .models import NFT, Listing


admin.site.register(NFT)
admin.site.register(Listing)
from django.shortcuts import render
from django.views.generic import CreateView
from .models import NFT

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def nfts_index(request):
    nfts = NFT.objects.all()
    return render(request, 'nfts/index.html', { 'nfts': nfts })

def nfts_detail(request, nft_id):
    nft = NFT.objects.get(id=nft_id)
    return render(request, 'nfts/detail.html', { 'nft': nft })

class NFTCreate(CreateView):
  model = NFT
  fields = '__all__'
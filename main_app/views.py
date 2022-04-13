from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
  success_url = '/nfts/'

class NFTUpdate(UpdateView):
  model = NFT
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'traits', 'number']

class NFTDelete(DeleteView):
  model = NFT
  success_url = '/nfts/'
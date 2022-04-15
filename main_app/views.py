from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import NFT
from .forms import ListingForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def nfts_index(request):
    nfts = NFT.objects.all()
    return render(request, 'nfts/index.html', { 'nfts': nfts })

def nfts_detail(request, nft_id):
    nft = NFT.objects.get(id=nft_id)
    listing_form = ListingForm()
    # return render(request, 'nfts/detail.html', { 'nft': nft })
    return render(request, 'nfts/detail.html', {
      'nft': nft, 'listing_form': listing_form
})

def add_listing(request, nft_id):
  form = ListingForm(request.POST)
  if form.is_valid():
    new_listing = form.save(commit=False)
    new_listing.nft_id = nft_id
    new_listing.save()
  return redirect('detail', nft_id=nft_id)

class NFTCreate(CreateView):
  model = NFT
  fields = '__all__'
  success_url = '/nfts/'

class NFTUpdate(UpdateView):
  model = NFT
  fields = ['breed', 'traits', 'number']

class NFTDelete(DeleteView):
  model = NFT
  success_url = '/nfts/'
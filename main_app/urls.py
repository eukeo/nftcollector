from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('nfts/', views.nfts_index, name='index'),
    path('nfts/<int:nft_id>/', views.nfts_detail, name='detail'),
    path('nfts/create/', views.NFTCreate.as_view(), name="nfts_create"),
    path('nfts/<int:pk>/update/', views.NFTUpdate.as_view(), name='nfts_update'),
    path('nfts/<int:pk>/delete/', views.NFTDelete.as_view(), name='nfts_delete'),
    path('nfts/<int:nft_id>/add_listing/', views.add_listing, name='add_listing'),
]
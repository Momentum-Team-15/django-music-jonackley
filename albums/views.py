from django.shortcuts import render
from .models import Album


# Create your views here.
def index(request):
    albums = Album.objects.all()
    return render(request, 'albums/index.html', {'albums':albums})

def album_detail(request, pk):
    album = Album.objects.get(pk=pk)
    return render(request, 'albums/album_detail.html', {'album':album})
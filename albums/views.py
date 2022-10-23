from django.shortcuts import render, redirect
from .models import Album, Song
from albums.forms import AlbumForm


# Create your views here.
def index(request):
    albums = Album.objects.all()
    return render(request, 'albums/index.html', {'albums':albums})

def album_detail(request, pk):
    album = Album.objects.get(pk=pk)
    return render(request, 'albums/album_detail.html', {'album': album})

def album_song_list(request, pk):
    song = Song.objects.get(pk=pk)
    return render(request, 'music/album_detail.html', {'song': song})

def create_album(request):
    if request.method == 'POST':
        # if user is submitting the form
        form = AlbumForm(request.POST)
        # form is the filled out ("bound") 
        # form with user data
        if form.is_valid():
            #django checks if form is valid (filled out with no missing
            # or mis-typed data)
            album = form.save()
            # because it's a ModelForm, saving it will create an
            # instance of Album in the database
            # only need commit=False if you are going to add additional 
            # data not on the form (like request.user)
            return redirect("home")
    else:
        form = AlbumForm()
        # if user is visiting a page with GET request, not submitting
        # the form yet, render a blank means
    return render(request, 'albums/create_album.html', {'form': form})

def album_delete(request):
    album =  Album.objects.get(pk=pk)
    return render(request
    'albums/ablum_delete.html',
    {'album':album})

def album_delete(request, id):
    album = Album.objects.get(id=id) # we need this for both GET and POST

    if request.method == 'POST':
        # delete the band from the database
        album.delete()
        # redirect to the bands list
        return redirect('albums')

    # no need for an `else` here. If it's a GET request, just continue

    return render(request,
                    'listings/album_delete.html',
                    {'album': album})

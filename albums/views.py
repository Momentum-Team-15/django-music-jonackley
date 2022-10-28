from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from albums.forms import AlbumForm


# Create your views here.
def index(request):
    albums = Album.objects.all()
    return render(request, 'albums/index.html', {'albums':albums})

def album_detail(request, pk):
    album = Album.objects.get(pk=pk)
    return render(request, 'albums/album_detail.html', {'album': album})

def create_album(request):
    if request.method == 'POST':
        # if user is submitting the form
        form = AlbumForm(request.POST)
        # form is the filled out ("bound")form with user data
        if form.is_valid():
            #django checks if form is valid (filled out with no missing or mis-typed data)
            album = form.save()
            # because it's a ModelForm, saving it will create an instance of Album in the database
            # only need commit=False if you are going to add additional data not on the form (like request.user)
            return redirect("home")
    else:
        form = AlbumForm()
        # if user is visiting a page with GET request, not submitting
        # the form yet, render a blank means
    return render(request, 'albums/create_album.html', {'form': form})

def album_delete(request, pk):
    post = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('home')
    return render(request, 'albums/album_delete.html', {'form': form})
    
def album_edit(request, pk):
    post = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('album_detail', pk=post.pk)
    else:
        form = AlbumForm(instance=post)
    return render(request, 'albums/album_edit.html', {'form': form})
                  

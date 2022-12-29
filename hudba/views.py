from django.db.models import Q
from django import forms
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from hudba.models import Album, Track, Review, Artist
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class Index(ListView):
    model = Album
    template_name = "index.html"


class AlbumList(ListView):
    model = Album
    context_object_name = "album_list"
    template_name = "albums/albums.html"
    paginate_by = 8

    ordering = ["-rating"]


class ArtistList(ListView):
    model = Artist
    context_object_name = "artist_list"
    template_name = "artists/artists.html"
    paginate_by = 5

    ordering = ["-name"]


class AlbumDetail(DetailView):
    model = Album

    context_object_name = "album_detail"
    template_name = "albums/detail.html"
    
    def get_context_data(self, **kwargs):
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        context["track_list"] = Track.objects.filter(album_id=self.kwargs['pk']).order_by("number")
        context["review_list"] = Review.objects.filter(reviewed_id=self.kwargs["pk"])
        return context


class ArtistDetail(DetailView):
    model = Artist

    context_object_name = "artists_detail"
    template_name = "artists/detail.html"

    def get_context_data(self, **kwargs):
        context = super(ArtistDetail, self).get_context_data(**kwargs)
        context["album_list"] = Album.objects.filter(artist_id=self.kwargs["pk"]).order_by("release_date")
        return context


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


class SearchResults(ListView):
    model = Album
    template_name = "search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("search")
        object_list = Album.objects.filter(
            Q(name__icontains=query) | Q(about__icontains=query)
        )
        return object_list


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def album_update(request, pk):
    album = Album.objects.get(id=pk)
    form = AlbumForm(instance=album)

    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES, instance=album)

        if form.is_valid():
            form.save()
            return redirect('album_detail', album.id)

    return render(request,
                  'albums/update.html',
                  {'form': form})


def album_delete(request, pk):
    album = Album.objects.get(id=pk)

    if request.method == 'POST':
        album.delete()
        return redirect('albums')

    return render(request, 'albums/delete.html',
                    {'album': album})


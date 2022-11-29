from django.db.models import Avg, Prefetch, Q
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

    ordering = ["-rating"]


class AlbumDetail(DetailView):
    model = Album

    context_object_name = "album_detail"
    template_name = "albums/detail.html"
    
    def get_context_data(self, **kwargs):
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        context["track_list"] = Track.objects.filter(album_id=self.kwargs['pk']).order_by("number")
        context["review_list"] = Review.objects.filter(reviewed_id=self.kwargs["pk"])
        return context


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
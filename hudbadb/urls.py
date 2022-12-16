"""hudbadb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from hudba import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.Index.as_view(), name="index"),
    path("albums/", views.AlbumList.as_view(), name="albums"),
    path("albums/<int:pk>/", views.AlbumDetail.as_view(), name="album_detail"),
    path("artists/", views.ArtistList.as_view(), name="artists"),
    path("artists/<int:pk>", views.ArtistDetail.as_view(), name="artists_detail"),
    path("search/", views.SearchResults.as_view(), name="search_results"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("albums/<int:pk>/update/", views.album_update, name="album_update"),
    path("albums/<int:pk>/delete/", views.album_delete, name="album_delete"),
    path("", include("django.contrib.auth.urls")),
    path('comment/', include('comment.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

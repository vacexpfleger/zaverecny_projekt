from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Origin(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.city}, {self.country}"


class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Members(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    role = models.ManyToManyField(Role)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Label(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=50)
    origin = models.ForeignKey(Origin, on_delete=models.CASCADE, blank=True, null=True)
    genre = models.ManyToManyField(Genre)
    members = models.ManyToManyField(Members)
    about = models.CharField(max_length=1000, blank=True, null=True)
    labels = models.ManyToManyField(Label)
    year_begin = models.DateField(blank=True, null=True)
    year_end = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to="albums/")
    about = models.TextField(max_length=1000)
    release_date = models.DateField()
    length = models.DurationField()
    rating = models.IntegerField(validators=[
        MaxValueValidator(100),
        MinValueValidator(0)
    ], blank=True, null=True)

    class Meta:
        ordering = ["-release_date"]

    def __str__(self):
        return self.name


class Track(models.Model):
    name = models.CharField(max_length=50)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    number = models.IntegerField()

    class Meta:
        ordering = ["number"]

    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media")

    def __str__(self):
        return str(self.image)


class Review(models.Model):
    reviewer = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[
        MaxValueValidator(100),
        MinValueValidator(1)
    ])
    text = models.CharField(max_length=500)
    reviewed = models.ForeignKey(Album, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-rating", "reviewer"]

    def __str__(self):
        return self.reviewer

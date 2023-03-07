from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class Band(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=150)
    band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name="album")

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=150)
    duration = models.DurationField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="song", null=True, blank=True)

def duration_as_str(self):
    minutes, seconds = divmod(self.duration.total_seconds(), 60)
    return f"{int(minutes)}:{int(seconds):02d}"

class AlbumReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="album_review")
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="album_review")
    content = models.TextField()
    score = models.CharField(max_length=5)

class AlbumReviewComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="album_review_comment")
    album_review = models.ForeignKey(AlbumReview, on_delete=models.CASCADE, related_name="album_review_comment")
    content = models.TextField()

class AlbumReviewLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="album_review_like")
    album_review = models.ForeignKey(AlbumReview, on_delete=models.CASCADE, related_name="album_review_like")



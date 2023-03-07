from rest_framework import serializers
from rest_framework import serializers
from .models import Band, Album, Song, AlbumReview, AlbumReviewComment, AlbumReviewLike

class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = ['id', 'name']

class AlbumSerializer(serializers.ModelSerializer):
    band_name = serializers.ReadOnlyField(source = 'band.name')

    class Meta:
        model = Album
        fields = ['id', 'name', 'band', 'band_name']


class SongSerializer(serializers.ModelSerializer):
    album_name = serializers.ReadOnlyField(source = 'album.name')
    band_name = serializers.ReadOnlyField(source = 'album.band.name')

    class Meta:
        model = Song
        fields = ['id', 'name', 'duration', 'album', 'album_name', 'band_name']


class AlbumReviewSerializer(serializers.ModelSerializer):
    album_name = serializers.ReadOnlyField(source='album.name')

    class Meta:
        model = AlbumReview
        fields = ['id', 'album', 'album_name', 'content', 'score']


class AlbumReviewCommentSerializer(serializers.ModelSerializer):
    album_name = serializers.ReadOnlyField(source='album_review.album.name')
    album_review_score = serializers.ReadOnlyField(source='album_review.score')
    user = serializers.ReadOnlyField(source='user.username')
    album_review = serializers.ReadOnlyField(source = 'album_review.id')

    class Meta:
        model = AlbumReviewComment
        fields = ['id', 'album_review', 'album_name', 'user', 'album_review_score', 'content']


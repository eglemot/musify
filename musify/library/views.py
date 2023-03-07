from rest_framework import generics, permissions
from . import models, serializers
from rest_framework.exceptions import ValidationError, PermissionDenied

class UserOwnedObjectRUDMixin():
    def delete(self, request, *args, **kwargs):
        obj = self.queryset.filter(pk=kwargs['pk'], user=request.user)
        if obj.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError(('Object not found or does not belong to you.'))

    def put(self, request, *args, **kwargs):
        obj = self.queryset.filter(pk=kwargs['pk'], user=request.user)
        if obj.exists():
            return self.update(request, *args, **kwargs)
        else:
            raise ValidationError(('Object not found or does not belong to you.'))
    
    def get_object(self):
        obj = super().get_object()
        if not obj.user == self.request.user:
            raise PermissionDenied("You do not have permission to perform this action.")
        return obj
    
class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser

class SuperuserManagedObjectRUDMixin():
    permission_classes = [IsSuperUser]
    def put(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user.is_superuser:
            return super().put(request, *args, **kwargs)
        else:
            raise PermissionDenied("You do not have permission to perform this action.")

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user.is_superuser:
            return super().delete(request, *args, **kwargs)
        else:
            raise PermissionDenied("You do not have permission to perform this action.")
    



class BandList(generics.ListCreateAPIView):
    serializer_class = serializers.BandSerializer
    queryset = models.Band.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BandDetail(SuperuserManagedObjectRUDMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.BandSerializer
    queryset = models.Band.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AlbumList(generics.ListCreateAPIView):
    serializer_class = serializers.AlbumSerializer
    queryset = models.Album.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AlbumDetail(SuperuserManagedObjectRUDMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.AlbumSerializer
    queryset = models.Album.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SongList(generics.ListCreateAPIView):
    serializer_class = serializers.SongSerializer
    queryset = models.Song.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SongDetail(SuperuserManagedObjectRUDMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.SongSerializer
    queryset = models.Song.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AlbumReviewList(generics.ListCreateAPIView):
    serializer_class = serializers.AlbumReviewSerializer
    queryset = models.AlbumReview.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AlbumReviewDetail(UserOwnedObjectRUDMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.AlbumReviewSerializer
    queryset = models.AlbumReview.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AlbumReviewCommentList(generics.ListCreateAPIView):
    serializer_class = serializers.AlbumReviewCommentSerializer
    queryset = models.AlbumReviewComment.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.validated_data['album_review'] = models.AlbumReview.objects.get(id=self.kwargs['album_review_id'])
        serializer.save()
    
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(album_review__id = self.kwargs['album_review_id'])
        return qs


class AlbumReviewCommentDetail(UserOwnedObjectRUDMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.AlbumReviewCommentSerializer
    queryset = models.AlbumReviewComment.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]




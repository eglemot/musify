from django.urls import path
from . import views

urlpatterns = [
    path('bands/', views.BandList.as_view(), name='band_list'),
    path('bands/<int:pk>/', views.BandDetail.as_view(), name='band-detail'),
    path('albums/', views.AlbumList.as_view(), name='album-list'),
    path('albums/<int:pk>/', views.AlbumDetail.as_view(), name='album-detail'),
    path('songs/', views.SongList.as_view(), name='song-list'),
    path('songs/<int:pk>/', views.SongDetail.as_view(), name='song-detail'),
    path('reviews/', views.AlbumReviewList.as_view(), name='album-review-list'),
    path('reviews/<int:pk>/', views.AlbumReviewDetail.as_view(), name='album-review-detail'),
    path('reviews/<int:album_review_id>/comments/', views.AlbumReviewCommentList.as_view(), name='album-review-comment-list'),
    path('comments/<int:pk>/', views.AlbumReviewCommentDetail.as_view(), name='album-review-comment-detail'),

]


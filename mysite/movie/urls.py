from .views import *
from django.urls import path




urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('', MovieListViewSet.as_view( {'get':'list','post': 'create'}),name='movie_list'),
    path('<int:pk>/', MovieDetailViewSet.as_view( {'get': 'retrieve'}),name='movie_detail'),

    path('user/', ProfileViewSet.as_view({'get': 'list','post': 'create'}), name='profile_list'),
    path('user/<int:pk>/', ProfileViewSet.as_view({'get': 'retrieve'}), name='profile_detail'),

    path('director/', DirectorViewSet.as_view({'get': 'list','post': 'create'}), name='director_list'),
    path('director/<int:pk>/', DirectorViewSet.as_view({'get': 'retrieve'}), name='director_detail'),


    path('actor/', ActorListViewSet.as_view({'get': 'list','post': 'create'}), name='actor_list'),
    path('actor/<int:pk>/', ActorDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                  'delete': 'destroy'}), name='actor_detail'),


    path('genre/', GenreViewSet.as_view({'get': 'list','post': 'create'}), name='genre_list'),
    path('genre/<int:pk>/', GenreViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                              'delete': 'destroy'}), name='movie_detail'),


    path('rating/', RatingViewSet.as_view({'get': 'list','post': 'create'}), name='rating_list'),
    path('rating/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                              'delete': 'destroy'}), name='movie_detail'),


    path('history/', HistoryViewSet.as_view({'get': 'list'}), name='history_list'),
    path('history/<int:pk>/', HistoryViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                              'delete': 'destroy'}), name='movie_detail'),


    path('favorite/', FavoriteViewSet.as_view({'get': 'list','post': 'create'}), name='favorite_list'),
    path('favorite/<int:pk>/',FavoriteViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                              'delete': 'destroy'}), name='movie_detail'),


    path('favoriteMovie/', FavoriteMovieViewSet.as_view({'get': 'list','post': 'create'}), name='favoriteMovie_list'),
    path('favoriteMovie/<int:pk>/',FavoriteMovieViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                              'delete': 'destroy'}), name='movie_detail'),


]
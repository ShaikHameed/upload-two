from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:post_id>/detail', views.detail, name='detail'),
	path('<int:post_id>/add_comment/', views.add_comment, name='add_comment'),
	path('<int:post_id>/add_like/', views.add_like, name='add_like'),
	path('pages', views.other_pages, name='other_pages'),
	path('movies', views.movies, name='movies'),
	path('conversations', views.conversations, name='conversations'),
	path('doodles', views.doodles, name='doodles'),
	path('videos', views.videos, name='videos'),
	path('shuffle', views.shuffle, name='shuffle'),
	path('search_site/', views.search_site, name='search_site'),
]
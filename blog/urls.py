from . import views
from django.urls import path
from .views import handler404, handler500, handler403, handler405


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add-book/', views.AddBook.as_view(), name='add-book'),
    path('books/', views.BookList.as_view(), name='books'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('book/edit/<slug:slug>/', views.EditBook.as_view(
        ), name='edit_book'),
    path('book/<slug:slug>/', views.BookDetail.as_view(), name='book_detail'),
    path('book/<slug:slug>/delete', views.BookDelete.as_view(
        ), name='book_delete')
]


handler404 = 'blog.views.handler404'
handler500 = 'blog.views.handler500'
handler403 = 'blog.views.handler403'
handler405 = 'blog.views.handler405'

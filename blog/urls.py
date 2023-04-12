from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add-book/', views.AddBook.as_view(), name='add-book'),
    path('books/', views.BookList.as_view(), name='books'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('<id>', views.BookDetail.as_view(), name='book_detail'),
]

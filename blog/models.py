from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django import forms
from bookclub import settings


STATUS = ((0, 'Draft'), (1, 'Published'))
BOOK_STATUS = ((0, 'Read'), (1, 'Currently Reading'), (
    2, 'Want to Read'), (3, 'Abandoned'))
RATING = ((0, 'unread'), (1, 'Very bad'), (2, 'Bad'), (
    3, 'Ok'), (4, 'Good'), (5, 'Very good'))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_post')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'


class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image_url = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=80)
    number_of_pages = models.IntegerField()
    category = models.CharField(max_length=80, unique=True)
    about = models.TextField()
    status = models.IntegerField(choices=BOOK_STATUS, default=2)
    rating = models.IntegerField(choices=RATING, default=0)
    data_started_reading = models.DateTimeField()
    date_finished_reading = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

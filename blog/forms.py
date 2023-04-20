from .models import Comment, Book
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'title',
            'slug',
            'image_url',
            'author',
            'number_of_pages',
            'category',
            'about',
            'rating',
            'data_started_reading',
            'date_finished_reading',
        )

from django.test import TestCase
from .forms import CommentForm, BookForm


class TestBookForm(TestCase):
    """
    Testing fields of the BookForm
    used for creating a book
    """
    def test_title_is_required(self):
        form = BookForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_slug_is_required(self):
        form = BookForm({'slug': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('slug', form.errors.keys())
        self.assertEqual(form.errors['slug'][0], 'This field is required.')

    def test_category_is_required(self):
        form = BookForm({'category': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('category', form.errors.keys())
        self.assertEqual(form.errors['category'][0], 'This field is required.')

    def test_image_url_is_not_required(self):
        form = BookForm({'image_url': ''})
        self.assertFalse(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = BookForm()
        self.assertEqual(form.Meta.fields, (
            'title',
            'slug',
            'image_url',
            'author',
            'number_of_pages',
            'category',
            'about',
            'status',
            'rating',
            'data_started_reading',
            'date_finished_reading',
        ))


class TestCommentForm(TestCase):
    """
    Testing fields of the CommentForm
    used for leaving a comment in a blog post
    """
    def test_body_is_required(self):
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')

    def test_field_is_explicit_in_form_metaclass(self):
        form = CommentForm()
        self.assertEqual(form.Meta.fields, ('body',))

from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import make_aware
from .models import Book, User
import pytz


class TestViews(TestCase):
    """
    Testing pageload and crud functionalities
    """
    def test_get_homepage(self):
        """
        Testing load homepage
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_books_page(self):
        """
        Testing load books page
        """
        response = self.client.get('/books/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_get_edit_book_page(self):
        """
        Testing edit a book
        """
        user = User.objects.create()
        book = Book.objects.create(
            title='teste',
            image_url='img',
            slug='teste',
            author='testador',
            number_of_pages=1,
            category='teste',
            about='bla-bla-bla',
            rating=1,
            data_started_reading='2011-10-05T14:48:00.000Z',
            date_finished_reading='2011-10-05T14:48:00.000Z',
            user=user
            )
        response = self.client.get(f'/book/edit/{book.slug}', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_can_add_book(self):
        """
        Testing create a book
        """
        user = User.objects.create()
        self.client.force_login(user)

        response = self.client.post('/add-book/', {
            'title': 'teste123',
            'image_url': 'img',
            'slug': 'teste123',
            'author': 'testador',
            'number_of_pages': 1,
            'category': 'teste123',
            'about': 'bla-bla-bla',
            'rating': 1,
            'status': 1,
            'data_started_reading':
                '2011-10-05T14:48:00.000Z',
            'date_finished_reading':
                '2011-10-05T14:48:00.000Z',
        })

        self.assertRedirects(response, reverse('books'), status_code=302)

        existing_book = Book.objects.filter(slug="teste123")
        self.assertEqual(len(existing_book), 1)

    def test_can_delete_book(self):
        """
        Testing delete a book
        """
        user = User.objects.create()
        self.client.force_login(user)
        book = Book.objects.create(
            title='teste',
            slug='teste',
            number_of_pages=1,
            category='teste',
            data_started_reading='2011-10-05T14:48:00.000Z',
            date_finished_reading='2011-10-05T14:48:00.000Z',
            user=user
            )
        response = self.client.get(f'/book/{book.slug}/delete', follow=True)
        self.assertRedirects(response, '/books/')
        existing_items = Book.objects.filter(slug=book.slug)
        self.assertEqual(len(existing_items), 0)

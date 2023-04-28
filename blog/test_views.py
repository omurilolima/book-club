from django.test import TestCase
from .models import Book, User


class TestViews(TestCase):
    """
    Testing pageload and crud functionalities
    """
    def test_get_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_books_page(self):
        response = self.client.get('/books/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_get_edit_book_page(self):
        user = User.objects.create()
        book = Book.objects.create(
            title='teste',
            slug='teste',
            number_of_pages=1,
            category='teste',
            data_started_reading='1999-01-01 01:01:00',
            date_finished_reading='1999-01-01 01:01:00',
            user=user
            )
        response = self.client.get(f'/book/edit/{book.slug}', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_can_add_book(self):
        user = User.objects.create()
        self.client.force_login(user)
        response = self.client.post('/add-book', {
            'title': 'teste',
            'slug': 'teste',
            'number_of_pages': 1,
            'category': 'teste',
            'data_started_reading': '1999-01-01 01:01:00',
            'date_finished_reading': '1999-01-01 01:01:00',
            'user': user,
        }, follow=True)
        self.assertRedirects(
            response, '/add-book/', status_code=301)

    def test_can_delete_book(self):
        user = User.objects.create()
        self.client.force_login(user)
        book = Book.objects.create(
            title='teste',
            slug='teste',
            number_of_pages=1,
            category='teste',
            data_started_reading='1999-01-01 01:01:00',
            date_finished_reading='1999-01-01 01:01:00',
            user=user
            )
        response = self.client.get(f'/book/{book.slug}/delete', follow=True)
        self.assertRedirects(response, '/books/')
        existing_items = Book.objects.filter(slug=book.slug)
        self.assertEqual(len(existing_items), 0)

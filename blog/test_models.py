from django.test import TestCase
from .models import Comment, Post, User


class TestViews(TestCase):
    def test_creating_a_comment(self):
        """
        Creating a comment
        """
        user = User.objects.create()
        post = Post.objects.create(
            title='Test',
            slug='test',
            author=user,
        )
        comment = Comment.objects.create(
            post=post,
            name=user.first_name,
            body='test comment for blog post'
        )
        # cheking the __str__() method
        # called by str()
        self.assertEqual(
            str(comment),
            f'Comment {comment.body} by {comment.name}')

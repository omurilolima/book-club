from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from .models import Post, Book
from .forms import CommentForm, BookForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if request.user.is_authenticated and post.likes.filter(id=self.request.user.id).exists():  # noqa
            liked = True

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': False,
                'liked': liked,
                'comment_form': CommentForm()
            }
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

        else:
            comment_form = CommentForm()

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'comments': comments,
                'commented': True,
                'liked': liked,
                'comment_form': CommentForm()
            }
        )


class PostLike(LoginRequiredMixin, View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class BookList(LoginRequiredMixin, generic.ListView):

    model = Book
    queryset = Book.objects.order_by('-created_on')
    template_name = 'books.html'
    paginate_by = 6

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)


class AddBook(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        return render(
                request,
                'add-book.html',
                {
                    'book_form': BookForm(),
                    'added_now': False,
                }
            )

    def post(self, request):

        book_form = BookForm(data=request.POST)
        messages.success(request, 'Book added')

        if book_form.is_valid():
            book_form.instance.user = request.user
            book_form.save()

        return HttpResponseRedirect(reverse('books'))


class EditBook(LoginRequiredMixin, View):

    def get(self, request, slug, *args, **kwargs):
        book = get_object_or_404(Book, slug=slug)
        book_form = BookForm(instance=book)

        return render(
            request,
            'edit_book.html',
            {
                'book_form': book_form,
                'edited': False,
            }
        )

    def post(self, request, slug, *args, **kwargs):

        book = get_object_or_404(Book, slug=slug)
        book_form = BookForm(request.POST, instance=book)
        messages.success(request, 'Book edited')

        # save the data from the form and
        # redirect to book_view
        if book_form.is_valid():
            print('Print do if')
            book_form.save()

            return HttpResponseRedirect(reverse('book_detail', args=[slug]))

            # return render(
            #     request,
            #     'book_detail.html',
            #     {
            #         'book': book,
            #         'edited': True,
            #     }
            # )

        return render(
            request,
            'edit_book.html',
            {
                'book_form': book_form,
            }
        )


class BookDetail(LoginRequiredMixin, View):

    def get(self, request, slug, *args, **kwargs):
        book = get_object_or_404(Book, slug=slug)

        return render(
            request,
            'book_detail.html',
            {
                'book': book,
            }
        )


class BookDelete(LoginRequiredMixin, View):

    def get(self, request, slug, *args, **kwargs):

        book = get_object_or_404(Book, slug=slug)
        book.delete()
        messages.success(request, 'Book deleted')

        return HttpResponseRedirect(reverse('books'))


def handler404(request, exception):
    """
    Custom 404 page
    """
    return render(request, "errors/404.html", status=404)


def handler500(request):
    """
    Custom 500 page
    """
    return render(request, "errors/500.html", status=500)


def handler403(request, exception):
    """
    Custom 403 page
    """
    return render(request, "errors/403.html", status=403)


def handler405(request, exception):
    """
    Custom 405 page
    """
    return render(request, "errors/405.html", status=405)

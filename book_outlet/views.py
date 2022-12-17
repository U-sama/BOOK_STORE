from django.shortcuts import render, get_object_or_404
from .models import Book
from django.http import Http404
from django.db.models import Avg, Sum, Max, Min

# Create your views here.

def index(request):
    books = Book.objects.all().order_by("-rating") # in decending add "-" before coulumn name
    total_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))["rating__avg"]  # rating__avg

    return render(request,"book_outlet/index.html", {
        "books":books,
        "total_books":total_books,
        "avg_rating":avg_rating
    })

def book_detail(request, slug):
    """ try:
        book = Book.objects.get(pk=id)
    except:
        raise Http404() """
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_detail.html", {
        "title":book.title,
        "author":book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling,
        "slug":book.slug
    })
from django.shortcuts import get_object_or_404, render
from .models import Book, Review


def show_main(request):
    return render(request, "index.html", {"books": Book.objects.all(),
                                          "reviews": Review.objects.all()})



def show_reviews(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)
    reviews = Review.objects.filter(book=book)
    return render(request, "reviews.html",{"book":book,
                                           "reviews": reviews})

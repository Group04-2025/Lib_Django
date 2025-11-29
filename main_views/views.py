from django.shortcuts import get_object_or_404, render
from .models import Book, Review


def show_main(request):
    books = Book.objects.all()
    genre_set = set()
    for book in books:
        genre_set.add(book.genre)
        
    return render(request, "index.html", {"books": Book.objects.all(),
                                          "reviews": Review.objects.all(),
                                          "genres": genre_set })


def show_genres(request, genre):
    books = Book.objects.filter(genre = genre)
    return render(request, "genre_page.html", {"books": books})


def show_reviews(request, title):
    book = Book.objects.get(title = title)
    reviews = Review.objects.filter(book = book)
    return render(request, "review_page.html", {"reviews": reviews})


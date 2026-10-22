from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.viewsets import ModelViewSet

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all().prefetch_related('book').only('id', 'full_name', 'birth_year','country')
    serializer_class = AuthorSerializer
    filter_backends =['id']

    ordering = '-id'

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends =[SearchFilter, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['id', 'price', 'published_year', 'pages']

    ordering = '-id'

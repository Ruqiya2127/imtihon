from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.viewsets import ViewSet

class AuthorViewSet(ViewSet):
    queryset = Author.objects.all().prefetch_related('book').only('id', 'full_name', 'birth_year','country')
    serializer_class = AuthorSerializer
    def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

class BookViewSet(ViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends =[SearchFilter, OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['price', 'published_year', 'pages']

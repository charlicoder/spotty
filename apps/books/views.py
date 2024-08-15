import time
from rest_framework import filters, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from .vectorizer import Vectorize

vc = Vectorize()



class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author__name']

    @action(detail=False, methods=['post'])
    def search_similarity(self, request):
        # import pdb; pdb.set_trace()
        query_title = request.data.get('title', None)
        if query_title is not None:
            start_time = time.time()
            ids = vc.search_similar_books(query_title, 5)
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Elapsed time: {elapsed_time} seconds. ids: {ids}")
            results = Book.objects.filter(id__in=ids)
            serializer = self.get_serializer(results, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Query parameter 'q' is required."}, status=status.HTTP_400_BAD_REQUEST)
    
from book.models import Book, Author, Library
from book.serializer import AuthorSerializer, BookSerializer, LeadsSerializer, LibrarySerializer
from book.form_validator import CreateBookValidator, UpdateBookValidator

from django.core import serializers

from rest_framework.views import APIView
from rest_framework.response import Response

class LibraryView(APIView):
    def get(self, request, id):
        library = Library.objects.get(pk=id)
        serializer = LibrarySerializer(library)
        return Response(serializer.data)

    def post(self, request, id):
        serializer = LibrarySerializer(data=request.data)
        if serializer.is_valid():
            new_library = serializer.save()
            library = LibrarySerializer(new_library).data
            return Response(library)
        else:
            return Response({"message": "form error"})

    def put(self, request, id):
        library_by_id = Library.objects.get(id=id)
        serializer = LibrarySerializer(instance=library_by_id, data=request.data)
        if serializer.is_valid():
            updated_library = serializer.save()
            library = LibrarySerializer(updated_library).data
            return Response(library)
        else:
            return Response({"message": "form error"})


class LibraryFilter(APIView):
    def get(self, request, **kwargs):
        library_id = kwargs["library_id"]
        book_id = kwargs["book_id"]

        libraries_by_id = Library.objects.get(pk=library_id)
        books_by_id = Book.objects.get(
            pk=book_id, libraries=library_id)
        serializedBooks = BookSerializer(books_by_id).data
        selectedLibrary = Library.objects.filter(
            id__in=serializedBooks["libraries"])
        print(selectedLibrary)
        serializedLibraries = LibrarySerializer(
            selectedLibrary, many=True).data

        return Response(serializedLibraries)


class BookListView(APIView):
    def get(self, request, id):
        book = Book.objects.get(pk=id)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def post(self, request, id):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            new_book = serializer.save()
            book = BookSerializer(new_book).data
            return Response(book)
        else:
            return Response({"message": "form error"})

    def put(self, request, id):
        book_by_id = Book.objects.get(id=id)
        serializer = BookSerializer(instance=book_by_id, data=request.data)
        if serializer.is_valid():
            updated_book = serializer.save()
            book = BookSerializer(updated_book).data
            return Response(book)
        else:
            return Response({"message": "form error"})


class BookSearch(APIView):
    def get(self, request):
        text = request.GET["text"]
        books_by_query = Book.objects.filter(title__contains=text)
        serialized_book = BookSerializer(books_by_query, many=True).data

        return Response(serialized_book)

class AuthorListView(APIView):
    def get(self, request, id):
        
        author = Author.objects.get(pk=id)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def post(self, request, id):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            new_author = serializer.save()
            author = AuthorSerializer(new_author).data
            return Response(author)
        else:
            return Response({"message": "form error"})

    def put(self, request, id):
        author_by_id = Author.objects.get(id=id)
        serializer = AuthorSerializer(instance=author_by_id, data=request.data)
        if serializer.is_valid():
            updated_author = serializer.save()
            author = AuthorSerializer(updated_author).data
            return Response(author)
        else:
            return Response({"message": "form error"})

class LeadsView(APIView):
    def post(self,request):
        print(request.data)
        serializer = LeadsSerializer(data=request.data)
        if serializer.is_valid():
            new_lead = serializer.save()
            lead = LeadsSerializer(new_lead).data
            return Response(lead)
        else:
            return Response({"message": "form error"})

library_view = LibraryView.as_view()
library_filter = LibraryFilter.as_view()
book_view = BookListView.as_view()
book_search = BookSearch.as_view()
author_list_view = AuthorListView.as_view()
leads_view = LeadsView.as_view()
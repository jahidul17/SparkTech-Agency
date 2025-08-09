from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from .import models
from .serializers import AuthorSerializer,CategoriesSerializer,BookSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsAdminOrReadOnly, IsAdmin

# Create your views here.
class AuthorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdmin]
    
    queryset=models.Author.objects.all()
    serializer_class=AuthorSerializer
    
    
class CategoriesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdmin]
    
    queryset=models.Categories.objects.all()
    serializer_class=CategoriesSerializer
    
    
class BookViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAdminOrReadOnly]
    
    queryset=models.Book.objects.all()
    serializer_class=BookSerializer
    
    def list(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())
    
        author = request.query_params.get('author')
        category = request.query_params.get('category')
        q = request.query_params.get('q')
        if author:
            qs = qs.filter(author__id=author)
        if category:
            qs = qs.filter(category__id=category)
        if q:
            qs = qs.filter(title__icontains=q)  # simple search
        page = self.paginate_queryset(qs)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)
    
class BookUpdateView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdmin]
    queryset = models.Book.objects.all()
    serializer_class = BookSerializer
    
  

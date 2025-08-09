from rest_framework import serializers

from .models import Author,Categories, Book
# from ..user.relations import PresentablePrimaryKeyRelatedField



class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields='__all__'
        
        
class CategoriesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Categories
        fields='__all__'
        
        
class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategoriesSerializer(read_only=True)
    
    class Meta:
        model = Book
        fields='__all__'
        
        






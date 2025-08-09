from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    bio = models.TextField(blank=True)


    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name_plural = "Author"
    
class Categories(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"
    

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    author = models.ManyToManyField(Author)
    category = models.ManyToManyField(Categories)  
    total_copies=models.IntegerField(blank=True,null=True)
    available_copies = models.IntegerField(blank=True,null=True)
    

    def __str__(self):
        return f"{self.title}"  
    
    class Meta:
        verbose_name_plural = "Book"
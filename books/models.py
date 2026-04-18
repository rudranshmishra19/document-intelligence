from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=500)
    author=models.CharField(max_length=300)
    rating=models.FloatField(null=True,blank=True)
    num_reviews=models.IntegerField(null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    genre=models.CharField(max_length=200,null=True,blank=True)
    summary=models.TextField(null=True,blank=True)
    book_url=models.URLField(max_length=500)
    price=models.CharField(max_length=50)
    language=models.CharField(max_length=20,null=True,blank=True)
    page_count=models.IntegerField(null=True,blank=True)
    dimensions_weight=models.FloatField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    availability=models.CharField(max_length=100,null=True,blank=True)


    def __str__(self):
        return self.title
    
    class Meta:
        ordering=['-created_at']




from django.db import models

# Create your models here.


class Blogs(models.Model):
    blog_title = models.CharField(max_length=20)
    blog_desc = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.blog_title
    
    
class Comments(models.Model):
    blog = models.ForeignKey(Blogs,on_delete=models.CASCADE,related_name='blog')
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.comment
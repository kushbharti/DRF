from .models import Blogs,Comments
from rest_framework import serializers



class Comments_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['comment','created_on','blog']
        

class Blogs_Serializer(serializers.ModelSerializer):
    blog = Comments_Serializer(many=True, read_only=True)
    class Meta:
        model = Blogs
        fields  = ['blog_title','blog_desc','created_on','blog']
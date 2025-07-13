from .models import Blogs,Comments
from .serializers import Blogs_Serializer,Comments_Serializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

# Create your views here.

class BlogsViewset(viewsets.ModelViewSet):
    queryset = Blogs.objects.all()
    serializer_class = Blogs_Serializer
    filter_backends = [SearchFilter]
    search_fields = ['blog_title']
    
    
class CommentsViewset(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = Comments_Serializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['blog']
  
from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'blogs',views.BlogsViewset)
router.register(r'comments',views.CommentsViewset)

urlpatterns = [
    path('',include(router.urls)),
]
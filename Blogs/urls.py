from django.urls import path,include
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

router = routers.DefaultRouter()
router.register(r'blogs',views.BlogsViewset)
router.register(r'comments',views.CommentsViewset)

urlpatterns = [
    path('',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='token_refresh'),
    path('verifytoken/',TokenVerifyView.as_view(),name='verify_token'),
]
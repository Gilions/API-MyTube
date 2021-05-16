from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

post_router = DefaultRouter()
comment_router = DefaultRouter()
group_router = DefaultRouter()
follow_router = DefaultRouter()

post_router.register('', PostViewSet, basename='post_list')
group_router.register('', GroupViewSet, basename='group_list')
follow_router.register('', FollowViewSet, basename='follow_list')
comment_router.register('comments', CommentViewSet, basename='comments_list')


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('group/', include(group_router.urls)),
    path('posts/', include(post_router.urls)),
    path('posts/<int:post_id>/', include(comment_router.urls)),
    path('follow/', include(follow_router.urls)),
]

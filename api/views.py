from django.shortcuts import get_object_or_404

from rest_framework import viewsets, permissions, filters

from .serializers import *
from .models import Post, Follow, Group, User
from .permissions import IsAuthorOrReadOnlyPermission


class PostViewSet(viewsets.ModelViewSet):
    """
    API для модели Post. Разрешенные методы:
    GET POST PUT PATCH DELETE
    """
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission,)

    def get_queryset(self):
        group = self.request.query_params.get('group')
        if group is not None:
            queryset = Post.objects.filter(group=group)
            return queryset
        queruset = Post.objects.all()
        return queruset

    def perform_create(self, serializer):

        # Создаем пост
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    API для модели Commet. Разрешенные методы:
    GET POST PUT PATCH DELETE
    """
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsAuthorOrReadOnlyPermission,)

    def get_queryset(self, *args, **kwargs):

        # Получаем комменты по id поста
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        queryset = post.comments.all()
        return queryset

    def perform_create(self, serializer):

        # Создаем новый коммент
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        if post is not None:
            serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API для модели Group. Разрешенные методы:
    GET POST
    """
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = (IsAuthorOrReadOnlyPermission,)
    http_method_names = ['get', 'post']


class FollowViewSet(viewsets.ModelViewSet):
    """
    API для модели Group. Разрешенные методы:
    GET POST
    """
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    http_method_names = ['get', 'post']
    permission_classes = (IsAuthorOrReadOnlyPermission,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['=following__username', '=user__username', ]

    def perform_create(self, serializer):

        # Проверяем валидность данных
        if 'following' not in self.request.POST:
            raise serializers.ValidationError('Validation Error!', code=400)
        username = self.request.data.get('following')
        following = User.objects.get(username=username)

        # Проверяем наличие подписки у Юзера
        value = Follow.objects.filter(user=self.request.user, following=following).exists()
        if self.request.user != following and value is not True:
            serializer.save(user=self.request.user, following=following)
        else:
            raise serializers.ValidationError('Validation Error!', code=400)

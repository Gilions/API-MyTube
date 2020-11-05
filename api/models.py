from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=200)


class Post(models.Model):
    objects = models.Manager()
    text = models.TextField()
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    group = models.ForeignKey(Group, models.SET_NULL, blank=True, null=True,
                              related_name="posts")

    def __str__(self):
        return self.text


class Comment(models.Model):
    objects = models.Manager()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created = models.DateTimeField("Дата добавления", auto_now_add=True, db_index=True)


class Follow(models.Model):
    objects = models.Manager()
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')

    class Meta:
        unique_together = ("user", "following",)

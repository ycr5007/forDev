from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Board(models.Model):
    title = models.CharField(max_length=256)
    writer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="write_board"
    )
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    like = models.ManyToManyField(
        User, related_name="like_board", blank=True, null=True
    )
    tags = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self) -> str:
        return self.title + " / " + self.writer.username

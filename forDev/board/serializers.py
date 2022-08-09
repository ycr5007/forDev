from dataclasses import fields
from rest_framework import serializers
from .models import Board
from user.models import Profile
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["image"]


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(many=False, read_only=True)

    class Meta:
        model = User
        fields = ["username", "profile"]


class BoardSerializer(serializers.ModelSerializer):
    writer = UserSerializer(many=False, read_only=True)
    # 태그 통계
    tag_cnt = serializers.SerializerMethodField("tag_cnt")
    # 태그 단어
    tag_word = serializers.SerializerMethodField("tag_word")

    def tag_cnt(self, board):
        pass

    def tag_word(self, board):
        pass

    class Meta:
        model = Board
        fields = [
            "id",
            "title",
            "created",
            "like",
            "writer",
            "tags",
            "tag_cnt",
            "tag_word",
        ]


class BoardContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ["id", "content"]

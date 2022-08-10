from dataclasses import fields
from rest_framework import serializers
from .models import Board
from user.models import Profile
from django.contrib.auth.models import User


class TagsSerializer(serializers.BaseSerializer):
    def to_representation(self, obj):
        return obj.split("#")[1:]


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
    tags = TagsSerializer()

    class Meta:
        model = Board
        fields = [
            "id",
            "title",
            "created",
            "like",
            "writer",
            "tags",
        ]


class BoardContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ["id", "content"]

from numpy import source
from rest_framework import serializers
from .models import Board
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]


class QuillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ["content"]


"""
def get_quill_field(string):
    delta = parse_html_to_delta(string) # HOW TO DO THIS?
    return Quill(
        '{"delta":"' + delta + '","html":"' + string + '"}')
"""


class BoardSerializer(serializers.ModelSerializer):
    writer = UserSerializer(many=False, read_only=True)
    # wirter_name = serializers.CharField(source="writer.username", read_only=True)

    class Meta:
        model = Board
        fields = [
            "id",
            "title",
            "content",
            "created",
            "like",
            "writer",
            "tags",
        ]

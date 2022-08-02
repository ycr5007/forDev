from rest_framework import generics
from django.shortcuts import get_object_or_404, redirect, render
from ..models import Board
from ..paginations import MyCursorPagination
from ..serializers import BoardSerializer


class IndexView(generics.ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    pagination_class = MyCursorPagination

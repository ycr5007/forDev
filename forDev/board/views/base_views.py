from rest_framework import generics
from django.shortcuts import get_object_or_404, redirect, render
from ..models import Board
from ..paginations import MyCursorPagination
from ..serializers import BoardSerializer

from django.contrib.auth.models import User


class IndexView(generics.ListAPIView):
    board = Board.objects.all()

    # 테스트 X
    # board_dict = {}
    # board_list = []
    # for bbs in board:
    #     board_dict["title"] = bbs.title
    #     board_dict["like"] = bbs.like.all
    #     board_dict["content"] = bbs.content
    #     board_dict["created"] = bbs.created
    #     board_dict["tags"] = bbs.tags
    #     board_dict["writer"] = bbs.writer.username
    #     board_list.append(board_dict)
    print(board.content)
    queryset = board
    serializer_class = BoardSerializer
    pagination_class = MyCursorPagination


def index(request):

    return render(request, "board/index.html")

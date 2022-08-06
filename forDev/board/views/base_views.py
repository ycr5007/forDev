from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json

from ..models import Board
from ..paginations import MyCursorPagination
from ..serializers import BoardContentSerializer, BoardSerializer
from ..forms import BoardForm


class IndexView(generics.ListAPIView):
    board = Board.objects.all()

    queryset = board
    serializer_class = BoardSerializer
    pagination_class = MyCursorPagination


class ContentView(APIView):
    def get(self, request, id):
        board = get_object_or_404(Board, pk=id)
        serializer = BoardContentSerializer(board)
        return Response(serializer.data, status=status.HTTP_200_OK)


@login_required(login_url="user:login")
def index(request):
    return render(request, "board/index.html")


def insert_board(request):
    if request.method == "POST":
        board = Board()
        board.title = request.POST.get("title")
        board.content = {"ops": json.loads(request.POST.get("content"))}
        board.writer = request.user
        board.save()
    return redirect("board:index")


# def test(request):
#     for i in range(100):
#         test_board = Board()
#         test_board.title = f"This Is TestCase [{i + 1}]"
#         test_board.content = {
#             "ops": [
#                 {"insert": "Gandalf", "attributes": {"bold": "true"}},
#                 {"insert": " the "},
#                 {"insert": "Grey", "attributes": {"color": "#cccccc"}},
#             ]
#         }
#         test_board.writer = request.user
#         test_board.save()

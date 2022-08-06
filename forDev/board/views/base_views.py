from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect, render

from ..models import Board
from ..paginations import MyCursorPagination
from ..serializers import BoardContentSerializer, BoardSerializer

from django.contrib.auth.models import User


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


def index(request):
    return render(request, "board/index.html")

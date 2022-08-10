from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
import json

from ..models import Board
from ..paginations import MyCursorPagination
from ..serializers import BoardContentSerializer, BoardSerializer, TagsSerializer

# from rest_pandas import PandasView


# class BoardDFVIew(PandasView):
#     board = Board.objects.all()

#     queryset = board
#     serializer_class = BoardSerializer
#     pagination_class = MyCursorPagination
#     # get()에 대한 응답으로 기본 Django REST Framework ListAPIView
#     # 는 기본 쿼리 세트(self.model.objects.all())를 로드한 다음
#     # 다음 함수에 전달합니다.
#     def filter_queryset(self, queryset):
#         # 이 시점에서 self.request 또는 다른
#         # 설정(메모리 사용을 제한하는 데 유용)을 기반으로 쿼리 집합을 필터링할 수 있습니다.
#         return queryset

#     # 그러면 포함된 PandasSerializer가 쿼리 세트를
#     # 간단한 사전 목록 목록으로 직렬화합니다(DRF ModelSerializer 사용). 포함할 # 필드 를 사용자 정의하려면
#     # PandasSerializer를 서브클래스로 만들고
#     # 적절한 ModelSerializer 옵션을 설정하십시오. 그런 다음 보기의 serializer_class
#     # 속성을 PandasSerializer 하위 클래스로 설정합니다.

#     # 다음으로 PandasSerializer는 ModelSerializer 결과를 DataFrame에 로드
#     # 하고 뷰의 다음 함수에 전달합니다.

#     def transform_dataframe(self, dataframe):
#         # 여기에서 self.request를 기반으로 데이터 프레임을 변환할 수 있습니다 .
#         # (피봇팅 또는 통계 계산에 유용함)
#         return dataframe

#     # 마지막으로 포함된 렌더러는 데이터 프레임을
#     # 아래의 출력 형식 중 하나로 처리합니다.


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
        board.tags = request.POST.get("tags")
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

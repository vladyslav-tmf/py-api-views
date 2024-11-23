from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from cinema.models import Genre
from cinema.serializers import GenreSerializer


class GenreList(APIView):
    @staticmethod
    def get(request: Request) -> Response:
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def post(request: Request) -> Response:
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GenreDetail(APIView):
    @staticmethod
    def get_object(pk: int) -> Genre:
        return get_object_or_404(Genre, pk=pk)

    def get(self, request: Request, pk: int) -> Response:
        serializer = GenreSerializer(self.get_object(pk=pk))
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request: Request, pk: int) -> Response:
        serializer = GenreSerializer(self.get_object(pk=pk), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    #  Possible, but pointless
    # def patch(self, request: Request, pk: int) -> Response:
        # serializer = GenreSerializer(
        #     self.get_object(pk=pk), data=request.data, partial=True
        # )
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request: Request, pk: int) -> Response:
        self.get_object(pk=pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

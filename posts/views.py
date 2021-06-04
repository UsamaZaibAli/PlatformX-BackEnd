from django.shortcuts import render
from django.http import HttpResponse
from .serializer import (CommentSerializer, PostSerializer, ImageSerializer)
from .models import Comment, Post, Image
from rest_framework import (viewsets, permissions, generics, status)
from rest_framework.response import Response
from rest_framework.decorators import (api_view, permission_classes)
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied, APIException
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from user.models import User


# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    try:
        response = {}

        serializer = PostSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            # print(serializer.is_valid(raise_exception=True))
            serializer.save()
            response["success"] = "Post has been created"
            return Response(data=response, status=status.HTTP_201_CREATED)

    except (PermissionDenied, APIException, KeyError) as e:
        response["error"] = "Post has not been created"
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_posts(request):
    try:
        response = {}
        # paginator = PageNumberPagination()
        # paginator.page_size = 2
        post = Post.objects.all()
        # result_page = paginator.paginate_queryset(post, request)
        # print(post)
        serializer = PostSerializer(post, many=True)
        # print(serializer.data)
        # return paginator.get_paginated_response(serializer.data)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    except AttributeError:
        response["error"] = "Error occured while gettings posts"
        return Response(data=response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CommentViewSet(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ImagesViewSet(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

# @api_view(['POST'])
# def create_post(request):
#     print(request)
#     return Response("This is the response")

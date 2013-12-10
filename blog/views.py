from blog.models import Article, Author, Comment
from rest_framework import viewsets
from blog.serializers import AuthorSerializer, ArticleSerializer, CommentSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    """
    Author API
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
    Article API
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    Comment API
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
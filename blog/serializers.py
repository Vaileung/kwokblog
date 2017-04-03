from django.contrib.auth.models import User
from rest_framework import serializers, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import permissions
from blog.models import Article, Category, Tag


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'body')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)


class ArticleSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = ArticleSerializer
    search_fields = 'title'

    def get_queryset(self):
        return Article.objects.all()

    def list(self, *args, **kwargs):
        queryset = Article.objects.all()
        search_param = self.request.query_params.get('title', None)
        if search_param is not None:
            queryset = Article.objects.filter(title__contains=search_param)

        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)


class CategorySet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = CategorySerializer


class TagSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    serializer_class = TagSerializer

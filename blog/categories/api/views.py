from rest_framework.viewsets import ModelViewSet
from categories.models import Category
from django_filters.rest_framework import DjangoFilterBackend
from categories.api.serializers import CategorySerializer
from categories.api.permissions import IsAdminOrReadOnly


class CategoryApiViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    queryset = Category.objects.all()
    #queryset = Category.objects.filter(published=False)
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']

from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from store.serializers import StoreSerializer, ProductSerializer
from store.models import Store, Product

from .documents import ProductDocument
import collections

class StoreViewSet(viewsets.ViewSet):
  def list(self, request):
    queryset = Store.objects.all()
    serializer = StoreSerializer(queryset, many=True)
    return Response(serializer.data)

  def retrieve(self, request, pk=None):
    queryset = ProductDocument.search().query("match", store=pk)
    data_list = []
    for a in queryset:
      d = {}
      d['pk'] = a.id
      d['title'] = a.title
      d['store'] = a.store
      data_list.append(d)
    return Response(data_list)
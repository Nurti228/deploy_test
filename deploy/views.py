from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import serializers
from . import models


@api_view(['GET'])
def product_list_view(request):
    products = models.Product.objects.all()
    data = serializers.ProductSerializer(products, many=True).data
    return Response(data=data)


@api_view(['GET'])
def test(request):
    context = {
        'integer': 100,
        'string': 'hello world',
        'boolean': True,
        'list': [
            1, 2, 3
        ]
    }
    return Response(data=context)

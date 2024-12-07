from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http.request import HttpRequest
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer
# Create your views here.

@api_view(["POST"])
def api_insert(request: HttpRequest, *args, **kwargs):
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid():
        return JsonResponse(serializer.data)


@api_view(["GET"])
def api_home(request:HttpRequest, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(model_data,fields=["id","price", "sale_price"])
        data = ProductSerializer(instance).data
    return JsonResponse(data)
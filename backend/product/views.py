from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http.request import HttpRequest
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import generics, mixins, permissions, authentication
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsStaffEditorPermission
# Create your views here.

class ProductMixinView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.CreateModelMixin, mixins.ListModelMixin,mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [IsStaffEditorPermission] # authenticated permission

    def perform_create(self, serializer:serializer_class):
        print(serializer.validated_data)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save( content= content)

        # send a django signal
        # return super().perform_create(serializer)

class ProductDetailAPIView(generics.RetrieveAPIView): # create rest api class
    queryset = Product.objects.all()
    # detail view basically help to look one single item
    serializer_class =ProductSerializer
    #lookupfield = 'pk'

class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    
    def perform_update(self, serializer:ProductSerializer):
        instance: Product = serializer.save()
        if not instance.content:
            instance.content = instance.title
            # instance.save()

class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"


    def perform_destroy(self, instance):
        # instance oeration

        super().perform_destroy(instance=instance)
        return JsonResponse({"message":"Success fully deleted the product"})



@api_view(["GET", "POST"])
def product_alt_view(request:HttpRequest,pk= None, *args, **kwargs):
    method = request.method
    if method == "GET":
        if pk is not None:
            # Detail view
            queryset = get_object_or_404 (Product, pk = pk)
            data = ProductSerializer(queryset).data
            return Response(data=data)

        else:
            qs= Product.objects.all()
            data = ProductSerializer(qs, many =True).data
            return Response(data=data)

        # list view, get request- > detail view
    elif method == "POST":
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content") or None
            if content is None:
                content = title
            serializer.save( content= content)
            return Response(serializer.data)


@api_view(["POST"])
def api_insert(request: HttpRequest, *args, **kwargs):
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        return JsonResponse(serializer.data)


@api_view(["GET"])
def api_home(request:HttpRequest, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(model_data,fields=["id","price", "sale_price"])
        data = ProductSerializer(instance).data
    return JsonResponse(data)
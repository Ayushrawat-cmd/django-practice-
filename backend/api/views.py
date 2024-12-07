from django.shortcuts import render
from django.http import JsonResponse, request
import json
# Create your views here.
def api_home(request:request.HttpRequest, *args, **kwargs):
    try:
        print(request.GET.keys())
        print(json.loads(request.body).keys()) # convert json to dictionary
    except :
        pass
    return JsonResponse({"message": "first response"})
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET"])
def api_home(request):
    data = {"message": "hello, world!"}
    return Response(data)

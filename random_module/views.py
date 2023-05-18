from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.generic.base import View
from .utils import get_random_module


class RandomModuleView(View):
    http_method_names = ["get"]

    def get(self, request):
        file = get_random_module()
        json = {
            'data': file.read(),
            'size': file.size,
            'classpath': file.classpath
        }
        return JsonResponse(json)

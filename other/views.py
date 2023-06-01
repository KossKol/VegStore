from django.shortcuts import render

from datetime import datetime

from django.views import View
from django.http import HttpResponse
from random import random


class CurrentDateView(View):
    def get(self, request):
        html = f"{datetime.now()}"
        return HttpResponse(html)


class RandomData(View):
    def get(self, request):
        random_number = {random()}
        return HttpResponse(random_number)


class HelloWorld(View):
    def get(self, request):
        str_a = f'{"""<h1>Hello, World</h1>"""}'
        return HttpResponse(str_a)

class IndexView(View):
    def get(self, request):
        return render(request, 'other/index.html')


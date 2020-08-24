import ast

from django.conf import settings
from django.http import HttpResponse, JsonResponse


class FuckingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        try:
            self.swear = settings.FUCKING_MIDDLEWARE_SWEAR
        except AttributeError:
            self.swear = "you fucking idiot"

    def __call__(self, request):
        response = self.get_response(request)
        content = response.content.decode('UTF-8')
        if isinstance(response, JsonResponse):
            content = ast.literal_eval(content)
            content = {f"{k}, {self.swear}": f"{v}, {self.swear}" for k, v in content.items()}
            response = JsonResponse(content)
        elif isinstance(response, HttpResponse):
            content = content.replace('</h1>', f', {self.swear}</h1>') \
                .replace('.\n', f', {self.swear}.\n') \
                .replace('. ', f', {self.swear}. ')
            response = HttpResponse(content)

        return response

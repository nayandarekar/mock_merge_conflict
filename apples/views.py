"""apple view docstring"""
from django.http import JsonResponse
from apples.models import Apple
from .serializers import serialize_apples


def apple_list(request):
    """list apple"""
    apples = Apple.objects.all()
    return JsonResponse(serialize_apples(apples), safe=False)

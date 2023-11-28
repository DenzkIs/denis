from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *


@api_view(['GET'])
def get_profile(request):
    profiles = Profile.objects.all()
    profile_serializer = ProfileSerializer(profiles, many=True)
    return Response({"profiles": profile_serializer.data})

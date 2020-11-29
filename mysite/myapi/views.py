from django.shortcuts import render
from .models import Hero
from .serializers import HeroSerializer
from rest_framework import viewsets


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer
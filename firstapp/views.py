from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Plan
from .serializers import PlanSerializer
from django.contrib.postgres.search import TrigramSimilarity

class PlanViewSet(ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    def get_queryset(self):
        soz = self.request.query_params.get("search")
        queryset = Plan.objects.all().annotate(similarity=TrigramSimilarity('sarlavha',
                soz)).filter(similarity__gte=0.5).order_by('-similarity')
        return queryset



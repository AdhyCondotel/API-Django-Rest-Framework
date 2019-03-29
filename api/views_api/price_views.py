from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from api.models import *
from api.serializers import *
from api.paginations import CustomResultsSetPagination
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet
from django_filters import rest_framework as filters

class PriceView(viewsets.ModelViewSet):
    queryset = Price.objects.all().order_by('created_at')
    serializer_class = PriceSerializer
    pagination_class = CustomResultsSetPagination

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            return Response({
                "detail" : "error", 
                "status_code": status.HTTP_400_BAD_REQUEST}, 
                status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            "detail" : "Success",
            "status_code": status.HTTP_201_CREATED
            }, status=status.HTTP_201_CREATED, headers=headers)

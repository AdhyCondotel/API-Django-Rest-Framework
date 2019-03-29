from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from api.models import *
from api.serializers import *
from api.paginations import CustomResultsSetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('email',)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({"detail" : "Success","status_code": status.HTTP_201_CREATED},
                status=status.HTTP_201_CREATED, headers=headers)

        return Response({"detail" : "error", "status_code": status.HTTP_400_BAD_REQUEST}, 
            status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid(raise_exception=False):
            self.perform_update(serializer)
            headers = self.get_success_headers(serializer.data)
            if getattr(instance, '_prefetched_objects_cache', None):
                instance._prefetched_objects_cache = {}
            return Response({"detail" : "Success","status_code": status.HTTP_202_ACCEPTED},
                status=status.HTTP_202_ACCEPTED, headers=headers)

        return Response({"detail" : "error", "status_code": status.HTTP_400_BAD_REQUEST}, 
            status=status.HTTP_400_BAD_REQUEST)    


    def partial_update(self, request, pk=None):
        return Response("partial_update data")


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"detail" : "Success","status_code": status.HTTP_204_NO_CONTENT},
            status=status.HTTP_204_NO_CONTENT)

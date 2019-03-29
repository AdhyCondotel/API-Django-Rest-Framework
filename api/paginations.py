from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    
    def get_paginated_response(self, data):
        return Response({
        	'results': data,
        	'meta': {
        	 	'count': self.page.paginator.count,
        	 	'total_pages': self.page.paginator.num_pages,
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            }
        })
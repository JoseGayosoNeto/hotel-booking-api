from math import ceil
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        total_items = self.page.paginator.count
        page_size = self.get_page_size(self.request)
        total_pages = ceil(total_items / page_size)
        return Response({
            'total_items': total_items,
            'total_pages': total_pages,
            'links': {
                'next': self.get_next_link(),
                'prev': self.get_previous_link()
            },
            'results': data
        })

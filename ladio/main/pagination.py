from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import PageNumberPagination

class LadioPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 10

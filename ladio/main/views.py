from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import list_route

from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator


from main.pagination import LadioPagination
from main.models import Content, Channel
from main.serializers import ContentSerializer, ChannelSerializer


class IndexView(TemplateView):
    template_name = 'base.html'



    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(IndexView,self).dispatch( *args, **kwargs)

class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class ContentViewSet(viewsets.ModelViewSet):
    serializer_class = ContentSerializer

    def get_queryset(self):
        # print("Request", repr(self.request.META))
        print("self.request.user", self.request.user)
        print("self.request.auth", self.request.auth)
        return Content.objects.all()


    @list_route(methods=['GET'])
    def recent_contents(self, request):
        recent_contents = Content.objects.all().order_by('-created')
        serializer = self.get_serializer(recent_contents, many=True)

        return Response(serializer.data)


#
# class TestModelViewSet(viewsets.ModelViewSet):
#     queryset = TestModel.objects.all()
#     serializer_class = TestModelSerializer
#     pagination_class = LadioPagination
#
#     @list_route(methods=['GET'])
#     def recent_contents(self, request):
#         recent_contents = TestModel.objects.all().order_by('-created')
#
#         page = self.paginate_queryset(recent_contents)
#         if page is not None:
#             print("none")
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
#
#         serializer = self.get_serializer(recent_contents, many=True)
#         return Response(serializer.data)
#



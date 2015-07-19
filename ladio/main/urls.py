from django.conf.urls import url, patterns
from rest_framework.routers import DefaultRouter

from main import views

urlpatterns = patterns('',
    )

router = DefaultRouter()
router.register(r'contents', views.ContentViewSet, 'content')
router.register(r'channels', views.ChannelViewSet)


urlpatterns += router.urls

#
# urlpatterns = patterns('',
#         # url(r'^$', index, name='index'),
#     )
#
# router = DefaultRouter()
# router.register(r'tests', views.TestModelViewSet)
#
# urlpatterns += router.urls
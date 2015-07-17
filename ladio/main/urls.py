from django.conf.urls import url, patterns
from django.views.generic import TemplateView

from rest_framework.routers import DefaultRouter

from main import views
from main.auth.views import UserViewSet, LoginView, LogoutView

urlpatterns = patterns('',
        url(r'^auth/login/$', LoginView.as_view(), name="login"),
        url(r'^auth/logout/$', LogoutView.as_view(), name="logout"),
    )

router = DefaultRouter()
router.register(r'users', UserViewSet)
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
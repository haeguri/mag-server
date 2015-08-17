from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from main.views import IndexView
from authentication.views import FacebookLogin
from main.admin import admin_root
from main.admin_staff import admin_staff

urlpatterns = [

    url(r'^auth/', include('authentication.urls')),
    url(r'^api/', include('main.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),

    url(r'^admin/', include(admin_root.urls)),
    url(r'^staff/admin/', include(admin_staff.urls)),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^$', IndexView.as_view(), name='inde'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
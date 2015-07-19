from django.conf.urls import url, patterns
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = patterns('',
        url(r'^auth/login/$', views.LoginView.as_view(), name="login"),
        url(r'^auth/logout/$', views.LogoutView.as_view(), name="logout"),
    )

router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns += router.urls
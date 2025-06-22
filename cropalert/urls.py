from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users.views import UserViewSet
from alerts.views import AlertViewSet
from alerts.views import alerts_page

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'alerts', AlertViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('alerts/', alerts_page, name='alerts-page'),
]

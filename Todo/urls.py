from django.contrib import admin
from django.urls import path, include
from firstapp.views import PlanViewSet
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

r = DefaultRouter()
r.register("plan", PlanViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Todo API for Codial Android developers",
      default_version='v1',
      description="Simple todo API that works with get, post, put, patch, delete methods.",
      contact=openapi.Contact('Abdulkhamid Egamberdiev, <abdulhamid97@gmail.com>'),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='docs'),
    path('', include(r.urls)),
]


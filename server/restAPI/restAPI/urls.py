from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from . import view
from api.views import StudentViewSet

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('students/', view.getDetails),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
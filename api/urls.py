from .views import UserViewSet
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router.register("users", UserViewSet, "users")

urlpatterns = router.urls

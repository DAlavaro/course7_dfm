# app/users/urls.py
from rest_framework.routers import SimpleRouter

from app.users.views import UserViewSet

router = SimpleRouter()
router.register('', UserViewSet)

urlpatterns = router.urls



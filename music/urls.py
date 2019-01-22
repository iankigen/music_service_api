from rest_framework import routers
from .views import SongsViewSets

router = routers.SimpleRouter()
router.register('songs', SongsViewSets)

urlpatterns = router.urls

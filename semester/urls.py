from rest_framework.routers import SimpleRouter
from . import views

app_name = 'semester'

router = SimpleRouter()
router.register("semester", views.SemesterViewSets, basename='api-semester')

urlpatterns = router.urls

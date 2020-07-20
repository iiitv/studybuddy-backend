from rest_framework.routers import SimpleRouter
from . import views

app_name = 'contribute'

router = SimpleRouter()
router.register("contribute", views.ContributeViewSets, basename='api-contribute')

urlpatterns = router.urls
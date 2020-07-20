from rest_framework.routers import SimpleRouter
from . import views

app_name = 'contact_us'

router = SimpleRouter()
router.register("contact", views.ContactViewSets, basename='api-contact')

urlpatterns = router.urls
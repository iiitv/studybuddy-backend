from rest_framework.routers import SimpleRouter
from . import views

app_name = 'course'

router = SimpleRouter()
router.register("course", views.CourseViewSets, basename='api-course')
router.register("assignment", views.AssignmentViewSets, basename='api-assignment')
router.register("exam", views.ExamPaperViewSets, basename='api-exam')
router.register("videolinks", views.VideoLectureViewSets, basename='api-videolinks')
router.register("notes", views.NoteViewSets, basename='api-notes')

urlpatterns = router.urls
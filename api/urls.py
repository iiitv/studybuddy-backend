from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls', namespace='rest-urls')),
    path('sem/', include('semester.urls', namespace='sem')),
    path('courses/', include('course.urls', namespace='course')),
    path('contacts/', include('contact_us.urls', namespace='contact')),
    path('contribute/', include('contribute.urls', namespace='contribute')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

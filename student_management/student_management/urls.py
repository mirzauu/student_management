
from django.urls import re_path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^accounts/', include(('account.urls', 'account'), namespace='accounts')),
    re_path(r'^teachers/', include(('teachers.urls', 'teachers'), namespace='teachers')),
    re_path(r'^students/', include(('students.urls', 'students'), namespace='students')),
    re_path(r'^api-auth/', include(('rest_framework.urls', 'rest_framework'), namespace='rest_framework')),
    re_path(r'^', include(('result.urls', 'result'), namespace='result')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

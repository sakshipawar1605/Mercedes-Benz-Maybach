from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import blog.views, projects.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',projects.views.home),
    path('blog/',blog.views.getallblogS),

] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
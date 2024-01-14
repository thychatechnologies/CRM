"""
URL configuration for BASE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler400,handler403,handler404,handler500

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('db/', admin.site.urls),
    path('',include('U_Auth.urls')),
    path('',include('ErrHandler.urls')),
    path('',include('Core.urls')),
    path('team/',include('Team.urls')),
    path('client/',include('Clients.urls')),
    path('project/',include('Projects.urls')),
    path('timesheet/',include('Timesheet.urls')),
    path('task/',include('Tasks.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler400 = 'ErrHandler.views.error_400'
handler403 = 'ErrHandler.views.error_403'
handler404 = 'ErrHandler.views.error_404'
handler500 = 'ErrHandler.views.error_500'

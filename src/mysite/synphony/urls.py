# chat/urls.py
from django.urls import re_path, path
from synphony import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # re_path(r'adgjlsfhk/getSongs', views.displaySongList, name='displaySongList'),
    re_path(r'adgjlsfhk/addSongs', views.addSongsToStudio, name='addSongs'),
    re_path(r'adgjlsfhk', views.index, name='index'),  # hard coded sharable link
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if not settings.DEBUG:
#     urlpatterns += [
#         url(r'^uploads/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
#         url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
#     ]
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

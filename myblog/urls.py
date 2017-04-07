"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.authtoken import views
from rest_framework import routers
from blog.serializers import ArticleSet, CategorySet, TagSet


apiRouter = routers.DefaultRouter()
apiRouter.register(r'article', ArticleSet, base_name='Article')
apiRouter.register(r'category', CategorySet)
apiRouter.register(r'tag', TagSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(apiRouter.urls)),
    url(r'^search/', include('haystack.urls')),
]

urlpatterns += staticfiles_urlpatterns()
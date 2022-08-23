"""HelloWorld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
#数据库操作
from django.urls import path, re_path
from . import views
#
# from . import views, testdb
#
# urlpatterns = [
#     path('runoob/', views.runoob),
#     path('testdb/', testdb.testdb),
# ]
#表单
# from django.conf.urls import url
# from . import views, testdb, search, search2
#
# urlpatterns = [
#     url(r'^hello/$', views.hello),
#     url(r'^testdb/$', testdb.testdb),
#     url(r'^search_form/$', search.search_form),
#     url(r'^search/$', search.search),
#     url(r'^search_post/$', search2.search_post),
#     path('runoob/', views.runoob),
# ]
urlpatterns = [
    # path('admin/', admin.site.urls),
    re_path("^index/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$", views.index),
    path('test/',views.test)
]
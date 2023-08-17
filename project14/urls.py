"""
URL configuration for project14 project.

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
from django.urls import path
from app.views import *
urlpatterns = [
    path("admin/", admin.site.urls),
    path('ass5/',ass5,name='ass5'),
    path('ass4/',ass4,name='ass4'),
    path('transform/',transform,name='transform'),
    path('transform1/',transform1,name='transform1'),
    path('timetable/',timetable,name='timetable'),
    path('registration/',registration,name='registration'),
    path('names/',names,name='names'),
    path('bg_styles_css/',bg_styles_css,name='bg_styles_css'),
    path('animate/',animate,name='animate'),
    path('pro_trans/',pro_trans,name='pro_trans'),
    path('online/',online,name='online'),
    path('boxmodel/',boxmodel,name='boxmodel'),
    path('birthday/',birthday,name='birthday'),
    path('bike/',bike,name='bike'),
    path('javajam/',javajam,name='javajam'),
]

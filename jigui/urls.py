#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""hequan URL Configuration

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

from django.conf.urls import url,include


from jigui.views import jigui, xiangxi, add, jigui_del,jigui_edit,show


urlpatterns = [
    url(r'^$',jigui),
    url(r'^jigui.html$', jigui ),
    url(r'^show.html$', show ),
    url(r'^xiangxi-(?P<nid>\d+).html$', xiangxi),
    url(r'^add.html$', add, name='addx'),
    url(r'^jiguidel-(?P<nid>\d+).html$', jigui_del),
    url(r'^jiguiedit-(?P<nid>\d+).html$', jigui_edit),
    ## url(r'^home',Home.as_view())   调用类里面的，如果是get调用get,post调用post

]


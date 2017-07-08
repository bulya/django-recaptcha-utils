# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from recaptcha_utils.urls import urlpatterns as recaptcha_utils_urls

urlpatterns = [
    url(r'^', include(recaptcha_utils_urls, namespace='recaptcha_utils')),
]

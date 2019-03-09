"""defop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include

from rest_framework import routers

from .api.viewsets import (
    PhoneNumberAPI,
)
from .views import index

router = routers.DefaultRouter()

router.register('phone_number', PhoneNumberAPI, base_name='phone_number')
# router.register('mandate', MandateAPI, base_name='mandate_request')
# router.register('contractor', ContractorAPI, base_name='contractor_request')
# router.register('caption', CaptionAPI, base_name='caption_request')
# router.register('theme', ThemeAPI, base_name='theme_request')
# router.register('execution', ExecutionAPI, base_name='execution_request')
# router.register(
#     'statehistory', StateHistoryAPI,
#     base_name='statehistory_request'
# )
# router.register(
#     'execution_report', ExecutionReportAPI,
#     base_name='execution_report_request'
# )
# router.register(
#     'mandate_type', MandateTypeAPI,
#     base_name='mandate_type_request'
# )
#

# urlpatterns = [
#     url(
#         r'^start_scrapy/?$',
#         login_required(start_scrapy), name='start_scrapy'
#     ),
#     url(
#         r'^start_import/?$',
#         login_required(start_import), name='start_import'
#     ),
#     # api
#
#     url(r'schema/?', login_required(schema_view)),
# ]



urlpatterns = [
    path('', index.as_view(), name='define_operator'),
    path('', include(router.urls)),
]

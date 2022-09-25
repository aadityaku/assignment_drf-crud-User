from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('',TodoView.as_view(),name='todo'),
    path('update/<int:id>/',TodoView.as_view(),name='update'),
    path('register/',Register.as_view(),name='register')
]
url_patterns=format_suffix_patterns(urlpatterns)
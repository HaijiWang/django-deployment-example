from django.conf.urls import url
from django.urls import path,include
from basic_app import views

# TEMPLATE TAGGING
app_name = 'basic_app_from_urls'

urlpatterns = [
    url(r'relative/', views.relative_view,name='relative'),
    url(r'other/',views.other_view,name='other')
]

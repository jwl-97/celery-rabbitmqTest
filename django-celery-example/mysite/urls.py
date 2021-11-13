from django.conf.urls import url
from mysite.core.views import TestAPIView

urlpatterns = [
    url('test', TestAPIView.as_view(), name='test')
]

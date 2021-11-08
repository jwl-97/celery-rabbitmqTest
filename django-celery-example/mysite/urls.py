from django.conf.urls import url
from mysite.core import views
from mysite.core.views import TestAPIView

urlpatterns = [
    url(r'^$', views.UsersListView.as_view(), name='users_list'),
    url(r'^generate/$', views.GenerateRandomUserView.as_view(), name='generate'),
    url('test', TestAPIView.as_view(), name='test'),
]

from django.conf.urls import url
from .views import other, relative

app_name = 'basic_app'
urlpatterns = [
    url(r'^relative/$', relative, name="relative"),
    url(r'^other/$', other, name="other"),
]

from django.conf.urls import url
from .views import register, user_login

app_name = "basic_app"
urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^user_login/$', user_login, name='user_login'),
]

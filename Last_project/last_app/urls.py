from django.conf.urls import url
from last_app import views

urlpatterns = [
     url(r'^$',views.users,name='users')
]

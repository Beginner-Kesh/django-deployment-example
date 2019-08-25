from django.conf.urls import url
from final_app import views


urlpatterns = [

    url(r'^$',views.next,name='next'),
]

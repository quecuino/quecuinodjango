from django.conf.urls import url,include
from . import views
from django.contrib.auth import views as auth_views
from quecuino.views import index,register
urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^registro/$',views.register, name='register'),
    url(r'^login/$',auth_views.login, name='login'),
    url(r'^like/$', views.like_receta, name='like_receta'),
    url(r'^(?P<id>\d+)/(?P<nom_recepta>[\w-]+)/$', views.post_detail, name='post_detail'),
]
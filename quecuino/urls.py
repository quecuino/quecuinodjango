from django.conf.urls import url,include
from . import views
from django.contrib.auth import views as auth_views
from quecuino.views import index,register
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^registre/$',views.register, name='register'),
    url(r'^login/$',auth_views.login, name='login'),
    url(r'^like/$', views.like_receta, name='like_receta'),
    url(r'^(?P<id>\d+)/(?P<slug>[\w-]+)/$', views.post_detail, name='post_detail'),
    url(r'^usuaris/(?P<usuario_id>\d+)/(?P<usuario>[\w-]+)/$', views.user_detail, name='user_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import  static
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    url('^$',views.home, name='home'   ),
    url(r'^task/new$',views.new_task,name = 'new_task'),
    url(r'^task/today$',views.do_today,name = 'do_today'),
    url(r'^task/(?P<pk>\d+)/update/', views.updateTask, name='updateTask'),
    url(r'^task/(?P<id>\d+)/delete/', views.deleteTask, name='deleteTask'),
    url(r'^confirm_delete/(\d+)',views.confirm_delete,name ='confirm_delete'),
    url(r'^api/task/$', views.TaskApi.as_view()),
    url(r'^api-token-auth/', obtain_auth_token),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

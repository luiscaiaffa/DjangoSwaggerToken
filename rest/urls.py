from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from rest import views

schema_view = get_swagger_view(title='Example Rest')

urlpatterns = [
 	url('^$', schema_view), 	
 	url(r'^user/list/$', views.UserList.as_view(), name="user-list"),
 	url(r'^user/list/token$', views.UserListToken.as_view(), name="user-list-token"),
]


# sxv95OcyHjSRKw4rtBclNVfbBAcW71
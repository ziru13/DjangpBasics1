# from django.conf.urls import url  # 旧版django
from django.urls import path
from . import views

app_name = "courses"

# make our variable, a list, in the old Django, it didn't use to be a list, now it's just a list
urlpatterns = [
    #path(r'', views.course_list, name='list'),  # I gave this the same url as our home page, it's not going to matter
    #path(r'(?P<course_pk>\d+)/(?P<step_pk>\d+)$', views.step_detail, name='step'),
    #path(r'(?P<pk>\d+)/$', views.course_detail, name='detail'),
    path('', views.course_list, name='course-list'),
    path('<int:course_pk>/<int:step_pk>', views.step_detail, name='step'),
    path('<int:pk>', views.course_detail, name='detail'),
]


# 给path添加一个name, 跟他们的html中的是一致的才可以
# https://teamtreehouse.com/community/noreversematch-reverse-for-viewshelloworld-not-found-viewshelloworld-is-not-a-valid-view-function-or-pattern-n

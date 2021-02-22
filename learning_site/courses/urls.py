from django.conf.urls import url

from . import views

# make our variable, a list, in the old Django, it didn't use to be a list, now it's just a list
urlpatterns = [
    url(r'^$', views.course_list),  # I gave this the same url as our home page, it's not going to matter
    url(r'(?P<course_pk>\d+)/(?P<step_pk>\d+)$', views.step_detail),
    url(r'(?P<pk>\d+)/$', views.course_detail),
]
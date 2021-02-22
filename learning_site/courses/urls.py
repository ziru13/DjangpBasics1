from django.conf.urls import url
from django.urls import path

from . import views

app_name = "courses"

# make our variable, a list, in the old Django, it didn't use to be a list, now it's just a list
urlpatterns = [
    # url(r'^$', views.course_list, name="course-list"),
    path('', views.course_list, name="course-list"),  # Django now recommends using "path". Also, you should add name="view-name"
    # url(r'(?P<course_pk>\d+)/(?P<step_pk>\d+)$', views.step_detail),
    path('<int:course_pk>/<int:step_pk>', views.step_detail), # Here's another example with "path"
    url(r'(?P<pk>\d+)/$', views.course_detail),
]
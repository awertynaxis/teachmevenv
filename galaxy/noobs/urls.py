from django.conf.urls import url
from django.urls import re_path, path

from .views import welcome, list_make_view, list_registration_view, \
    list_createtask_view, update_task_view, delete_task_view, \
    archive_task_date_view, list_task_view, archive_task_today_view, \
    list_completed_view, list_uncompleted_view, login_view, list_room_view, details_room_view

urlpatterns = [
    url('^welcome$', welcome, name='welcome'),
    path('room/', list_room_view, name ='room'),
    re_path('^room/(?P<pk>\d+)',details_room_view , name='room-details'),
    url('^show_registration', list_make_view, name='show_registration'),
    url('^registration', list_registration_view, name='registration'),
    url('^login', login_view, name='login'),
    url('^createtask', list_createtask_view, name='createtask'),
    re_path('^updatetask/(?P<pk>\d+)', update_task_view, name='updatetask'),
    re_path('^deletetask/(?P<pk>\d+)', delete_task_view, name='deletetask'),
    path('archive_task_date/<int:year>/<int:month>/<int:day>', archive_task_date_view, name='archive_task_date'),
    re_path('^show_task_detail/(?P<pk>\d+)', list_task_view, name='show_task_detail'),
    path('today/', archive_task_today_view, name='today'),
    path('show_completed_detail/completed', list_completed_view, name='show_completed_detail/completed'),
    path('show_completed_detail/uncompleted', list_uncompleted_view, name='show_completed_detail/uncompleted')
]

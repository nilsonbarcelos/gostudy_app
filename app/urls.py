from django.contrib import admin
from django.urls import path
from .views.course_view import *
from .views.user_view import *

urlpatterns = [
    path('', course_list, name='course_list'),
    path('course_list/', course_list, name='course_list'),
    path('add_course', add_course, name='add_course'),
    path('edit_course/<int:id>', edit_course, name="edit_course"),
    path('delete_course/<int:id>', delete_course, name="delete_course"),
    path('add_user/', add_user, name="add_user"),
    path('user_login/', user_login, name="user_login"),
    path('user_logout/', user_logout, name="user_logout"),
]

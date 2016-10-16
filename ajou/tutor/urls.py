from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_handler, name='login'),
    url(r'^logout/$', views.logout_handler, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^board/teacher$', views.board_teacher, name='board.teacher'),
    url(r'^board/student$', views.board_student, name='board.student'),
]

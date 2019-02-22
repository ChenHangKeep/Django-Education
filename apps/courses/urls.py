# -*- coding: utf-8 -*-
__author__ = 'bobby'

from django.conf.urls import url, include

from .views import CourseListView, CourseDetailView,CourseInfoView,CourseCommentView,AddCommentView,VideoPlayView

urlpatterns = [
    #课程列表页
    url(r'^list/$', CourseListView.as_view(), name="course_list"),

    #课程详情页
    # url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="course_detail"),
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="course_detail"),
    url(r'^info/(?P<course_id>\d+)/$',CourseInfoView.as_view(),name="course_info"),
    url(r'^comment/(?P<course_id>\d+)/$',CourseCommentView.as_view(),name='course_comment'),
    url(r'^add_comment/$',AddCommentView.as_view(),name='add_comment'),
    url(r'^video/(?P<video_id>\d+)/$',VideoPlayView.as_view(),name='video_play')

    #
    # url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name="course_info"),
    #
    # #课程评论
    # url(r'^comment/(?P<course_id>\d+)/$', CommentsView.as_view(), name="course_comments"),
    #
    # #添加课程评论
    # url(r'^add_comment/$', AddComentsView.as_view(), name="add_comment"),

]
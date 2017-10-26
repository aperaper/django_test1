#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Xry'

import xadmin

from .models import Course, Lesson, Video, CourseResource, BannerCourse
from organization.models import CourseOrg


class LessonInline(object):
    model = Lesson
    extra = 0


class CourseResourceInline(object):
    model = CourseResource
    extra = 0


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'stu_nums', 'favor_nums', 'get_capture_nums',
                    'go_to']  # 默认显示哪些项目
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'stu_nums', 'favor_nums', 'image',
                     'click_nums']  # 搜索栏
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'stu_nums', 'favor_nums', 'image', 'click_nums',
                   'add_time']  # 筛选字段
    ordering = ['-click_nums']
    # readonly_fields = ['fav_nums']  # 不可修改
    list_editable = ['degree', 'detail']
    exclude = ['click_nums']  # 不可见
    inlines = [LessonInline, CourseResourceInline]
    # refresh_times = [3, 5]
    # style_fields = {'detail': 'ueditor'}
    import_excel = True

    def queryset(self):
        qs = super(CourseAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs

    def save_models(self):
        # 在保存课程的时候统计课程机构的课程数
        obj = self.new_obj  # 取到新增课程的实例
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org  # 从course对象中取外键course_org
            course_org.course_nums = Course.objects.filter(course_org=course_org).count()
            course_org.save()

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            pass
        return super(CourseAdmin, self).post(request, *args, **kwargs)

class BannerCourseAdmin(object):
    list_display = ['name', 'detail', 'degree', 'learn_times', 'stu_nums', 'favor_nums']  # 默认显示哪些项目
    search_fields = ['name', 'detail', 'degree', 'learn_times', 'stu_nums', 'favor_nums', 'image', 'click_nums']  # 搜索栏
    list_filter = ['name', 'detail', 'degree', 'learn_times', 'stu_nums', 'favor_nums', 'image', 'click_nums',
                   'add_time']  # 筛选字段
    ordering = ['-click_nums']
    # readonly_fields = ['fav_nums']  # 不可修改
    exclude = ['click_nums']  # 不可见
    inlines = [LessonInline, CourseResourceInline]

    def queryset(self):
        qs = super(BannerCourseAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)

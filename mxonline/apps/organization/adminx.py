#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Xry'

import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']  # 默认显示哪些项目
    search_fields = ['name', 'desc']  # 搜索栏
    list_filter = ['name', 'desc', 'add_time']  # 筛选字段


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fav_nums', 'address', 'city']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city', 'add_time']
    relfield_style = 'fk-ajax' #将下拉框设置为搜索状态


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums',
                    'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums',
                   'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)

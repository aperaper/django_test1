#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Xry'

import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from .models import EmailVerifyRecord, Banner, UserProfile


# def get_form_layout(self):
#     if self.org_obj:
#         self.form_layout = (
#             Main(
#                 Fieldset('',
#                          'username', 'password',
#                          css_class='unsort no_title'
#                          ),
#                 Fieldset(_('Personal info'),
#                          Row('first_name', 'last_name'),
#                          'email'
#                          ),
#                 Fieldset(_('Permissions'),
#                          'groups', 'user_permissions'
#                          ),
#                 Fieldset(_('Important dates'),
#                          'last_login', 'date_joined'
#                          ),
#             ),
#             Side(
#                 Fieldset(_('Status'),
#                          'is_active', 'is_staff', 'is_superuser',
#                          ),
#             )
#         )
#     return super(UserAdmin, self).get_form_layout()
#

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = 'xx后台管理系统'
    site_footer = 'xx网'
    menu_style = 'accordion'


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time', ]  # 默认显示哪些项目
    search_fields = ['code', 'email', 'send_type']  # 搜索栏
    list_filter = ['code', 'email', 'send_type', 'send_time', ]  # 筛选字段
    model_icon = "fa fa-address-book-o"


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


# 卸载和注册User以及UserProfile
# from django.contrib.auth.models import User
# xadmin.site.unregister(User)

# class UserProfileAdmin(UserAdmin):
#     pass
# xadmin.site.register(UserProfile, UserProfileAdmin)


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

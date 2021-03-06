from datetime import datetime

from django.db import models
from organization.models import CourseOrg, Teacher
# from DjangoUeditor.models import UEditorField


# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='课程名')
    need_know = models.CharField(default='', max_length=300, verbose_name='课程须知')
    teacher_tell = models.CharField(default='', max_length=300, verbose_name='老师告诉你')
    desc = models.CharField(max_length=300, verbose_name='课程描述')
    detail = models.TextField(verbose_name='课程详情')
    is_banner = models.BooleanField(default=False, verbose_name='是否轮播')
    teacher = models.ForeignKey(Teacher, verbose_name='讲师', null=True, blank=True)
    degree = models.CharField(verbose_name='难度', choices=(('primary', '初级'), ('middle', '中级'), ('high', '高级')),
                              max_length=7)
    learn_times = models.IntegerField(default=0, verbose_name='学习时长(分钟数)')
    stu_nums = models.IntegerField(default=0, verbose_name='学习人数')
    favor_nums = models.IntegerField(default=0, verbose_name='收藏')
    image = models.ImageField(upload_to='courses/%Y/%m', verbose_name='封面图', max_length=100)
    click_nums = models.IntegerField(default=0, verbose_name='点击数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    course_org = models.ForeignKey(CourseOrg, verbose_name='课程机构', null=True)
    category = models.CharField(default='后端开发', max_length=20, verbose_name='课程类别')
    tag = models.CharField(default='', verbose_name='课程标签', max_length=50)

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def get_capture_nums(self):
        # 获取课程章节数
        all_lessons = self.lesson_set.all().count()

    get_capture_nums.short_description = '章节数'

    def go_to(self):
        from django.utils.safestring import mark_safe
        return mark_safe("<a href='http://www.baidu.com'>跳转</>")

    go_to.short_description = '跳转'

    def get_learn_users(self):
        return self.usercourse_set.all()[:5]

    def get_chapter(self):
        # 获取课程章节
        return self.lesson_set.all()

    def __str__(self):
        return self.name


class BannerCourse(Course):
    class Meta:
        verbose_name = '轮播课程'
        verbose_name_plural = verbose_name
        proxy = True


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='章节名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name

    def get_video(self):
        # 获取章节视频
        return self.video_set.all()

    def __str__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name='章节')
    name = models.CharField(max_length=100, verbose_name='视频名')
    url = models.URLField(default='', max_length=300, verbose_name='访问视频地址')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    learn_times = models.IntegerField(default=0, verbose_name='学习时长(分钟数)')

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='视频名')
    download = models.FileField(upload_to='course/resource/%Y/%m', verbose_name='资源文件', max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name

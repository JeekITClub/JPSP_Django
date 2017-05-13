# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    grade = models.IntegerField()
    classroom = models.IntegerField()
    attend_year = models.CharField(max_length=4)
    club = models.TextField()
    lftlip = models.TextField()
    # lftlip ->last_five_loginin_time


class Club(models.Model):
    name = models.CharField(max_length=30)
    clubid = models.CharField(max_length=4)
    # 社团id
    proprieter = models.IntegerField()
    # 社长的QQ
    if_enroll = models.BooleanField()
    # 是否进行招新
    enroll_group_qq = models.IntegerField()
    # 招新QQ群号
    email = models.EmailField()
    label = models.TextField()
    state = models.BooleanField()
    # 该社团是否已成立
    stars = models.IntegerField()
    introduction = models.TextField()
    # 社团介绍
    achievements = models.TextField()


class post(models.Model):
    author = models.ForeignKey(Club)


class message(models.Model):
    from_user = models.ForeignKey(User)
    send_time = models.DateField(auto_now=True)
    to_user = models.CharField(max_length=30)
    read_time = models.DateField(auto_now_add=True)
    message_type = (
        ('nm', '需要进行社团打分'),
    )
    type = models.CharField(max_length=3, choices=message_type)
    content = models.TextField(default='')


class stars(models.Model):
    club = models.ForeignKey(Club)
    week = models.CharField(max_length=2)
    # 第几周
    time = models.CharField(max_length=2)
    # 第几次社团活动
    year = models.CharField(max_length=6)
    # year 第几学年 格式为 2016-2
    stars = models.FloatField()
    star_time = models.DateField(auto_now=True)
    # 字段保存时会自动保存当前时间
    times = models.CharField(max_length=3)


class post_request(models.Model):
    from_user = models.CharField(max_length=30)
    open_time = models.DateField(auto_now=True)
    request_content = models.TextField()
    close_time = models.DateField()

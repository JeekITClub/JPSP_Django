# coding=utf-8
from __future__ import unicode_literals
from django.db import models


# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=30)
    password = models.TextField()
    grade = models.IntegerField()
    classroom = models.IntegerField()
    attend_year=models.IntegerField()
    # attend_year ->attend_school_year
    club=models.TextField()
    lftlip=models.TextField()
    # lftlip ->last_five_loginin_time


class club(models.Model):
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


class comment(models.Model):
    author = models.ForeignKey(user)
    content = models.TextField()
    ip = models.CharField(max_length=15)
    comment_datetime = models.DateField(auto_now_add=True)
    # comment_post_id
    # comment datetime


class post(models.Model):
    author = models.ForeignKey(club)
    title = models.CharField(max_length=30)
    post_time = models.DateField()
    # post_time为文章批准发布在网站上的时间
    add_time = models.DateField(auto_now_add=True)
    # add_time字段在实例第一次保存的时候会保存当前时间
    edit_time = models.DateField(auto_now=True)
    # 字段保存时会自动保存当前时间
    status = models.BooleanField()
    # 文章是草稿/还未批准/被禁止发布状态是status的值为False ，已经发布了则为True
    # comment = models.ForeignKey(comment)
    # comment 为该文章的评论，暂时不开启评论功能
    # category_choice=(
    #     (),
    # )
    # category = models.CharField(max_length=1,choices=category_choice)
    category = models.CharField(max_length=1)
    # 文章的分类
    # TODO: 确定文章有哪些分类
    content = models.TextField()


class message(models.Model):
    from_user = models.ForeignKey(user)
    send_time = models.DateField(auto_now=True)
    to_user = models.CharField(max_length=30)
    read_time = models.DateField(auto_now_add=True)
    message_type = (
        ('nm', '需要进行社团打分'),
    )
    type = models.CharField(max_length=3, choices=message_type)
    content = models.TextField(default='')


class stars(models.Model):
    stars = models.FloatField()
    star_time = models.DateField(auto_now=True)
    # 字段保存时会自动保存当前时间
    times = models.CharField(max_length=3)


class post_request(models.Model):
    from_user = models.CharField(max_length=30)
    open_time = models.DateField(auto_now=True)
    request_content = models.TextField()
    close_time = models.DateField()

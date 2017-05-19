# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(User)
    grade = models.IntegerField()
    classroom = models.IntegerField()
    attend_year = models.CharField(max_length=4,default="2016")
    club = models.TextField()
    lftlip = models.TextField(default="")
    # lftlip ->last_five_loginin_time


class CDUser(models.Model):
    user=models.ForeignKey(User)


class Club(models.Model):
    name = models.CharField(max_length=30)
    clubid = models.CharField(max_length=4)
    # 社团id
    shezhang_name = models.CharField(max_length=8,default="")
    shezhang_qq = models.CharField(max_length=20,default="")
    # 社长的QQ
    if_recruit = models.BooleanField()
    # 是否进行招新
    enroll_group_qq = models.CharField(max_length=20,default="")
    # 招新QQ群号
    email = models.EmailField()
    label = models.TextField(default="")
    state = models.BooleanField()
    # 该社团是否已成立
    stars = models.IntegerField(default=0)
    introduction = models.TextField(default="")
    # 社团介绍
    achievements = models.TextField(default="")


class Post(models.Model):
    #ClubName = models.ForeignKey(Club)
    LinkmanGrade = models.CharField(max_length=1,default="1")
    LinkmanClass = models.CharField(max_length=2,default="1")
    LinkmanName = models.CharField(max_length=8,default="")
    LinkmanPhoneNumber = models.CharField(max_length=11,default="00000000000")
    LinkmanQq = models.CharField(max_length=20,default="00000000")
    Region = models.CharField(max_length=30,default="00000")
    Date1 = models.DateField(default=None)
    Date2 = models.TimeField(default=None)
    Process = models.TextField(default="")
    Content = models.TextField(default="")
    Assessment = models.TextField(default="")
    Feeling = models.TextField(default="")
    Stars = models.FloatField(default=0.0)
    StarTime = models.DateTimeField(default=None)


class Message(models.Model):
    from_user = models.ForeignKey(User)
    send_time = models.DateField(auto_now=True)
    to_user = models.CharField(max_length=30)
    read_time = models.DateField(default=None)
    message_type = (
        ('nm', '需要进行社团打分'),
    )
    type = models.CharField(max_length=3, choices=message_type)
    content = models.TextField(default='')
# TODO: edit the message model


class Token(models.Model):
    token = models.TextField()
    user = models.ForeignKey(User)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

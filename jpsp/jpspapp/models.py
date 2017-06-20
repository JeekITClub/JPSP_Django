# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Settings(models.Model):
    name = models.CharField(max_length=10, default="settings")
    clubid = models.IntegerField()


class UserProfile(models.Model):
    UserName = models.ForeignKey(User)
    StudyID = models.CharField(max_length=8, default="")
    Grade = models.IntegerField()
    Classroom = models.IntegerField()
    AttendYear = models.CharField(max_length=4, default="2016")
    Club = models.TextField()
    Lftlip = models.TextField(default="")
    # lftlip ->last_five_loginin_time


class CDUser(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=30, default="社团部")


class Club(models.Model):
    ClubName = models.CharField(max_length=30, default="社团")
    ClubId = models.ForeignKey(User)
    # 社团id
    ShezhangName = models.CharField(max_length=8, default="")
    ShezhangQq = models.CharField(max_length=20, default="")
    ShezhangGrade = models.CharField(max_length=1, default="")
    ShezhangClassroom = models.CharField(max_length=2, default="")
    # 社长的QQ
    IfRecruit = models.BooleanField()
    # 是否进行招新
    EnrollGroupQq = models.CharField(max_length=20, default="")
    # 招新QQ群号
    Email = models.EmailField()
    Label = models.TextField(default="")
    State = models.BooleanField()
    # 该社团是否已成立
    Stars = models.IntegerField(default=0)
    Introduction = models.TextField(default="")
    # 社团介绍
    Achievements = models.TextField(default="")


class Post(models.Model):
    ClubName = models.CharField(max_length=30, default="社团")
    CludId = models.ForeignKey(Club)
    LinkmanGrade = models.CharField(max_length=1, default="1")
    LinkmanClass = models.CharField(max_length=2, default="1")
    LinkmanName = models.CharField(max_length=8, default="")
    LinkmanPhoneNumber = models.CharField(max_length=11, default="00000000000")
    LinkmanQq = models.CharField(max_length=20, default="00000000")
    Region = models.CharField(max_length=30, default="00000")
    Date1 = models.DateField(default=None)
    Date2 = models.TimeField(default=None)
    Process = models.TextField(default="")
    Content = models.TextField(default="")
    Assessment = models.TextField(default="")
    Feeling = models.TextField(default="")
    Stars = models.FloatField(default=0.0)
    StarTime = models.DateTimeField(default=None)
    IfPass= models.BooleanField(default=False)

class Message(models.Model):
    from_user = models.ForeignKey(User)
    send_time = models.DateTimeField(auto_now=True)
    to_user = models.CharField(max_length=30)
    read_time = models.DateTimeField(default=None)
    message_type = (
        ('cps', '需要进行社团活动进行打分'),
        ('ca', '需要审核社团活动'),
        ('ce', '需要审核社团建立')
    )
    type = models.CharField(max_length=3, choices=message_type)
    content = models.TextField(default='')


class Token(models.Model):
    token = models.CharField(max_length=30, default="")
    username = models.ForeignKey(User)
    usertype_choices = (
        ('club', 'club'),
        ('cd', 'club_department'),
        ('s', 'student'),
        ('t', 'teacher')
    )
    usertype = models.CharField(max_length=4, choices=usertype_choices)
    # start_time = models.DateTimeField()
    # end_time = models.DateTimeField()


class Activity(models.Model):
    ActivityName = models.CharField(max_length=30, default="活动名称")
    Region = models.CharField(max_length=30, default="活动地点")
    ClubId = models.ForeignKey(Club)
    ClubName = models.CharField(max_length=30, default="社团")
    Content = models.TextField(default="活动内容")
    Date1 = models.DateTimeField()
    # Date1 is start datetime
    Date2 = models.DateTimeField()
    # Date2 is end datetime
    state_choices = (
        ('0', 'Draft'),
        ('1', 'Accepted'),
        ('2', 'Denied')
    )
    State = models.CharField(max_length=1, choices=state_choices, default='0')
    type_choices = (
        ('0', '普通'),
        ('1', '义卖'),
        ('2', '销售'),
    )
    Type = models.TextField(default='0', choices=type_choices)
    Participants = models.TextField(default="")


class Classroom(models.Model):
    ClassroomId = models.IntegerField()
    ClubId = models.ForeignKey(Club)
    ClubName = models.CharField(max_length=30, default="社团")
    Date1 = models.DateTimeField()
    Date2 = models.DateTimeField()


class LostAndFound(models.Model):
    LostOrFound = models.CharField(max_length=4, default="丢失")
    LinkmanName = models.CharField(max_length=30, default="匿名")
    LinkmanGrade = models.CharField(max_length=1, default="0")
    LinkmanClassroom = models.CharField(max_length=2, default="0")
    LinkmanPhoneNumber = models.CharField(max_length=11, default="0000000000")
    LinkmanQq = models.CharField(max_length=20, default="0")
    LostObjectName = models.CharField(max_length=100, default="")
    LostPlace = models.CharField(max_length=30, default="")
    Importacne = models.BooleanField(default=False)
    Desc = models.TextField(default="")
    LostDateTime = models.DateTimeField()

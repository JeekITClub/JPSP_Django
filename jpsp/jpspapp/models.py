# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Settings(models.Model):
    name = models.CharField(max_length=10, default="settings")
    clubid = models.IntegerField()


class UserProfile(models.Model):
    UserObject = models.ForeignKey(User, default=None)
    UserName = models.CharField(max_length=12, default=None)
    Grade = models.IntegerField()
    Class = models.IntegerField()
    AttendYear = models.CharField(max_length=4, default="2016")
    Lftlip = models.TextField(default="")
    QQ = models.CharField(max_length=12, default=None)
    Phone = models.CharField(max_length=12, default=None)
    Email = models.EmailField()
    # lftlip ->last_five_loginin_time


class CDUser(models.Model):
    user = models.ForeignKey(User)
    username = models.CharField(max_length=30, default="社团部")


class Club(models.Model):
    ClubName = models.CharField(max_length=30, default="社团")
    # ClubObject = models.ForeignKey(User,default=User.objects.get(username=''))
    ClubId = models.CharField(max_length=4, default=None)
    ShezhangName = models.CharField(max_length=8, default="")
    ShezhangQq = models.CharField(max_length=20, default="")
    ShezhangGrade = models.CharField(max_length=1, default="")
    ShezhangClass = models.CharField(max_length=2, default="")
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
    Member = models.TextField(default="")
    # TODO: Member many to many field?


class Post(models.Model):
    ClubName = models.CharField(max_length=30, default="社团")
    CludId = models.ForeignKey(Club, default=None)
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
    Pass = models.CharField(max_length=1,default='1')
    # Pass中有3个选项，未审核为0，被拒绝为1，通过为2


class Message(models.Model):
    FromUser = models.ForeignKey(User)
    SendTime = models.DateTimeField(auto_now=True)
    ToUser = models.CharField(max_length=30)
    ReadTime = models.DateTimeField(default=None)
    message_type = (
        ('cps', '需要进行社团活动进行打分'),
        ('ca', '需要审核社团活动'),
        ('ce', '需要审核社团建立'),
        ('default', 'default')
    )
    Type = models.CharField(max_length=3, choices=message_type, default='default')
    Content = models.TextField(default='')


class Token(models.Model):
    Token = models.CharField(max_length=30, default="")
    UserName = models.ForeignKey(User)
    usertype_choices = (
        ('club', 'club'),
        ('cd', 'club_department'),
        ('s', 'student'),
        ('t', 'teacher')
    )
    UserType = models.CharField(max_length=4, choices=usertype_choices, default=None)
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
    Participants = models.ManyToManyField(UserProfile)


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
    LinkmanClass= models.CharField(max_length=2, default="0")
    LinkmanPhoneNumber = models.CharField(max_length=11, default="0000000000")
    LinkmanQq = models.CharField(max_length=20, default="0")
    LostObjectName = models.CharField(max_length=100, default="")
    LostPlace = models.CharField(max_length=30, default="")
    Importacne = models.BooleanField(default=False)
    Desc = models.TextField(default="")
    LostDateTime = models.DateTimeField()

class Event(models.Model):
    Name = models.CharField(max_length=30,default=None)
    Date = models.DateTimeField()
    Region =models.CharField(max_length=30,default=None)
    Content = models.TextField(default=None)
    Club = models.ForeignKey(Club)
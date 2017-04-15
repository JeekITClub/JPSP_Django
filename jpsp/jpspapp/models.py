from __future__ import unicode_literals
from django.db import models

# Create your models here.

class user(models.Model):
    name=models.CharField(max_length=30)
    #password=
    #grade
    classroom=models.IntegerField()
    #attend_year ->attend_school_year
    #club
    #lftlip ->last_five_loginin_time


class club(models.Model):
    name=models.CharField(max_length=30)
    proprieter=models.IntegerField()
    if_enroll=models.BooleanField()
    enroll_group_qq=models.IntegerField()
    email=models.EmailField()
    label=models.TextField()
    # TODO:  make 'label' ->tuple
    state=models.BooleanField()
    stars=models.IntegerField()
    introduction=models.TextField()


class comment(models.Model):
    pass
# comment_post_id
# comment datetime
# content
# author
# author_ip


class post(models.Model):
    author = models.ForeignKey(club)
    title = models.CharField(max_length=30)
    post_time = models.DateField()
    add_time = models.DateField(auto_now_add=True)
    edit_time = models.DateField(auto_now=True)
    status = models.BooleanField()
    comment = models.ForeignKey(comment)
    category = models.CharField(max_length=30)
    content = models.TextField()
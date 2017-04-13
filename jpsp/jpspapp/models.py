from __future__ import unicode_literals
from django.db import models

# Create your models here.

class user(models.Model):
    name=models.CharFiled(max_length=30)
    #password=
    #grade
    classroom=models.IntegarField()
    #attend_year ->attend_school_year
    #club
    #lftlip ->last_five_loginin_time

class club(models.Model):
    name=models.CharFiled(max_length=30)
    proprieter=models.CharFiled(max=length=10)
    proprieter=models.IntegarField()
    if_enroll=models.BooleanFiled()
    enroll_group_qq=models.IntegarField()
    email=models.EmailField()
    label=models.TextField()
    # TODO:  make 'label' ->tuple
    state=models.BooleanFiled()
    stars=models.IntegarField()
    introduction=models.TextField()

class post(models.Model):
    author=models.ForeignKey(club)
    title=models.CharFiled(max_length=30)
    post_time=models.DateField()
    add_time=models.DateField(auto_now_add=true)
    edit_time=models.DateField(auto_now=true)
    status=models.BooleanFiled()
    comment=models.ForeignKey(comment)
    category=models.CharFiled()
    content=models.TextField()

class comment(models.Model):
    #comment_post_id
    #comment datetime
    #content
    #author
    #author_ip

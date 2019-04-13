#coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
import datetime


# Create your models here.

'''
定义数据模型，即数据库表的设计和其他附加的元数据
(元数据：定义数据所需要的数据，例如搜索歌曲时，歌曲本身数数据，但是可以通过歌名、作者、专辑等元数据搜索这首歌)
'''

class Question(models.Model):
    question_text = models.CharField(default=u'',max_length=200)
    pub_date = models.DateTimeField('date published')

    '''该函数目的是为了在admin后台管理页面中显示添加的对象'''

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __unicode__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    '''这里的外键定义了一个关系，告诉django每一个Choice对象都关联到一个Question对象。这里的on_delete是一个级联操作
    即如果主表数据被删除，那么从表数据也会被删除'''
    choice_text = models.CharField(max_length=200,default=u'')
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text

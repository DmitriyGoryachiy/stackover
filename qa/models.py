# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from Categories.models import Category
# Create your models here.


class Question(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length = 255, verbose_name = u'Тема вопроса')
    text = models.TextField(default = '')
    createdate = models.DateTimeField(auto_now_add = True)
    updatedate = models.DateTimeField(auto_now = True)
    categories = models.ManyToManyField(Category, related_name = 'questions')
    is_deleted = models.BooleanField(default = False)
    likecount = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

    class Meta:
       ordering = '-createdate',
       verbose_name = u'Вопрос'
       verbose_name_plural = u'Вопросы'



class Answer(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    question = models.ForeignKey('qa.Question', related_name = 'answers')
    text = models.TextField(default = '')
    createdate = models.DateTimeField(auto_now_add=True)
    #updatedate = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'{}({})'.format(self.id,self.question.title)

    class Meta:
       verbose_name = u'Ответ'
       verbose_name_plural = u'Ответы'
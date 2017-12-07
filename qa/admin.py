# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Question, Answer


# Register your models here.
class AnswersInLine(admin.TabularInline):

   model = Answer


class QuestionsInLine(admin.TabularInline):

    model = Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):

    list_display = 'id','title', 'createdate',
    list_editable = 'title',
    inlines = AnswersInLine,


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):

    pass




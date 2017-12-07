# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Category
from django.contrib import admin

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = 'id', 'title'
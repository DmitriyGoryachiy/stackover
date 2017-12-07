# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import DetailView
from django.shortcuts import render
from .models import Category

# Create your views here.
class CategoryDetail(DetailView):

    template_name = 'Categories/Category_detail.html'
    context_object_name = 'category'
    model = Category

    def get_queryset(self):
        q = super(CategoryDetail, self).get_queryset()
        q = q.order_by(self.request.GET.get('order_by','title'))
        if 'search' in self.request.GET:
            q = q.filter(title=self.request.GET['search'])
        return q
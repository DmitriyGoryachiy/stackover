# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.shortcuts import render, reverse, HttpResponse
from django import forms
from django.views import View
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Question, Answer
import json


class QuestionLikes(View):

    def get(self, request):
        ids = request.GET.get('ids','')
        ids = ids.split(',')
        questions = dict(Question.objects.filter(id__in=ids).values_list('id','likecount'))
        return JsonResponse(questions)


class QuestionLikesCountView(View):

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.question = get_object_or_404(Question, pk=pk)
        return super(QuestionLikesCountView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return HttpResponse (self.question.likecount)

    def post(self, request):
        self.question.likecount += 1
        self.question.save()
        return HttpResponse (self.question.likecount)


class QuestionUpdate(View):
    #
    # context_object_name = 'question'
    # model = Question
    # template_name = 'qa/Update_question.html'
    # fields = 'title', 'text'

    def dispatch(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        qw = get_object_or_404(Question, pk=pk)
        author = qw.author
        user = self.request.user
        # print (author, user)
        if user == author:
            return super(QuestionUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied("DENIED")

    # def get_success_url(self):
    #     # return super(QuestionUpdate,self).get_success_url()
    #     # return reverse('', kwargs={'pk': self.object.pk})
    #     return reverse('qa:question_detail', kwargs={'pk': self.object.pk})





class NewQuestion(CreateView):

    template_name = 'qa/new_question.html'
    model = Question
    fields = 'title', 'text'

    def get_success_url(self):
        return reverse('qa:question_detail', kwargs={'pk':self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(NewQuestion,self).form_valid(form)


# class mainQuestionDetail(CreateView):
#
#     template_name = 'qa/main_question_detail.html'
#     context_object_name = 'question'
#     model = Question
#     fields = ['title','text']


class QuestionDetail(CreateView):

    template_name = 'qa/question_detail.html'
    context_object_name = 'question'
    model = Answer
    fields = ['text']

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        qw = get_object_or_404(Question,pk=pk)
        context = super(QuestionDetail, self).get_context_data(**kwargs)
        context['question'] = qw
        return context



    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.question_id = self.kwargs.get('pk')
        return super(QuestionDetail,self).form_valid(form)

    def get_success_url(self):
        return reverse('qa:question_detail', kwargs={'pk': self.kwargs.get('pk')})


    # def post(self, request):
    #     self.question.title= '1'
    #     self.question.text='abracadabra'
    #     self.question.save()
    #     return reverse('qa:question_detail', kwargs={'pk': self.kwargs.get('pk')})


class QuestionListForm(forms.Form):
    order_by = forms.ChoiceField(choices=(
        ('title','title'),
        ('-title','-title'),
        ('id','id'),
    ),required=False)
    search = forms.CharField(required=False)

    # def autocompleteModel(request):
    #     search_qs = Question.objects.filter(title__startswith=request.GET['search'])
    #     results = []
    #     for r in search_qs:
    #         results.append(r.email)
    #     resp = request.GET['callback'] + '(' + simplejson.dumps(results) + ');'
    #     return HttpResponse(resp, content_type='application/json')



class MainPage(ListView):

    template_name = 'qa/MainPage.html'
    context_object_name = 'questions'
    model = Question
    paginate_by = 5

    def get_queryset(self):
        q = super(MainPage, self).get_queryset().order_by('-createdate')
        return q


class QuestionList(ListView):

    template_name = 'qa/questions.html'
    context_object_name = 'questions'
    model = Question
    paginate_by = 10

    def get_queryset(self):
        q = super(QuestionList, self).get_queryset()
        form = QuestionListForm(self.request.GET)
        if form.is_valid():
            if form.cleaned_data['order_by']:
                q = q.order_by(form.cleaned_data['order_by'])
            if form.cleaned_data['search']:
                q = q.filter(title=self.request.GET['search'])
        return q





from django.conf.urls import url
from qa import views
from qa.views import QuestionDetail, QuestionList, MainPage, QuestionLikesCountView, QuestionLikes
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^questions/new/$', login_required(views.NewQuestion.as_view()), name='new_question'),
    url(r'^questions/(?P<pk>\d+)$', QuestionDetail.as_view(), name='question_detail'),
    url(r'^questions/(?P<pk>\d+)/edit/$', login_required(views.QuestionUpdate.as_view()), name='question_update'),
    url(r'^questions/$', QuestionList.as_view(), name='questions'),
    url(r'^$', MainPage.as_view(), name='index'),
    url(r'^questions/(?P<pk>\d+)/likes/$', login_required(QuestionLikesCountView.as_view()), name='question_like_count'),
    url(r'likes/$',QuestionLikes.as_view(), name='likes'),
    # url(r'^search-autocomplete/$', autocompleteModel,  name='search-autocomplete'),
]

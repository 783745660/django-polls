#coding=utf-8
from django.shortcuts import render,get_object_or_404   #快捷函数
from django.http import Http404
from django.template import loader
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Question,Choice #从models中导入数据表，视图函数会从数据表中抽取数据对象，然后用模板表示出现
# Create your views here.
'''
编写视图函数，用于返回http响应
'''
from django.http import HttpResponse,HttpResponseRedirect

'''
视图函数只会做两件事：
    1返回一个包含被请求页面内容的对象HttpResponse；2抛出一个异常；
'''
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DateDetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DateDetailView):
    model = Question
    template_name = 'polls/results.html'



def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice =  question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':"you don't select a choice",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(question.id)))
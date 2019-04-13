#coding=utf-8
__author__ = 'CoderSong'
__date__ = '2019/4/12 13:12'

'''
该urls.py用于将views.py中的视图函数与urls.py做一个映射:
    每次用户发过来的请求，Django会用URL_pattern与请求进行匹配，
    匹配到第一个URL_pattern，就会把请求转向对于的view
'''
from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'), #这里当匹配到hello时，调用views.index
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(),name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(),name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote,name='vote'),
]



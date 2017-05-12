# coding=utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from jpspapp import function
import json

# Create your views here.



# index

def index(request):
    template = loader.get_template('index.html')
    content = {}
    return HttpResponse(template.render(content, request))


# login

def login(request):
    template = loader.get_template('login.html')
    content = {}
    return HttpResponse(template.render(content, request))


# admin

def admin(request):
    template = loader.get_template('admin/index.html')
    get = function.admin_content()
    # content=get.get_base_content()
    content = {}
    return HttpResponse(template.render(content, request))


def admin_login(request):
    template = loader.get_template('admin/login.html')
    content = {}
    return HttpResponse(template.render(content, request))


def admin_post_overview(request):
    template = loader.get_template('admin/post/overview.html')
    get = function.admin_content()
    content = get.get_base_content()
    return HttpResponse(template.render(content, request))


def admin_post_verify(request):
    # 用来进行对提出申请发布的动态的批准页1
    template = loader.get_template('admin/post/verify.html')
    get = function.admin_content()
    content = get.get_base_content()
    return HttpResponse(template.render(content, request))


def admin_post_edit(request):
    template = loader.get_template('admin/post/edit.html')
    get = function.admin_content()
    content = get.get_base_content()
    return HttpResponse(template.render(content, request))


def admin_post_denied(request):
    template = loader.get_template('admin/post/denied.html')
    content = {'username': '社团部'}
    return HttpResponse(template.render(content, request))


def admin_post_analysis(request):
    template = loader.get_template('admin/post/analysis.html')
    get = function.admin_content()
    content = get.get_base_content()
    return HttpResponse(template.render(content, request))


def admin_stars_overview(request):
    template = loader.get_template('admin/stars/overview.html')
    get = function.admin_content()
    content = get.get_base_content()
    return HttpResponse(template.render(content, request))


def admin_stars_mark(request):
    template = loader.get_template('admin/stars/mark.html')
    get = function.admin_content()
    content = get.get_base_content()
    return HttpResponse(template.render(content, request))


def admin_stars_marked(request):
    template = loader.get_template('admin/stars/marked.html')
    get = function.admin_content()
    content = get.get_base_content()
    return HttpResponse(template.render(content, request))


def admin_stars_history(request):
    template = loader.get_template('admin/stars/history.html')
    get = function.admin_content()
    content = get.get_base_content()
    return HttpResponse(template.render(content, request))


def admin_message_overview(request):
    template = loader.get_template('admin/message/overview.html')
    get = function.admin_content()
    content = get.get_base_content()
    return HttpResponse(template.render(content, request))


def admin_message_read(request):
    # 已读信息
    template = loader.get_template('admin/message/read.html')
    get = function.admin_content()
    content = get.get_base_content()
    return HttpResponse(template.render(content, request))


def admin_message_unread(request):
    template = loader.get_template('admin/message/unread.html')
    get = function.admin_content()
    content = get.get_base_content()
    return HttpResponse(template.render(content, request))


def admin_message_history(request):
    template = loader.get_template('admin/message/history.html')
    get = function.admin_content()
    content = get.get_base_content()
    return HttpResponse(template.render(content, request))


def register(request):
    template = loader.get_template('register.html')

    # 用来进行对提出申请发布的动态的批准页1
    template = loader.get_template('admin/post/verify.html')
    content = {}
    return HttpResponse(template.render(content, request))


# club

def club_clubs(request):
    clubs = ''
    # 所有社团
    template = loader.get_template('club/clubs.html')
    content = {'clubs': clubs}
    return HttpResponse(template.render(content, request))


def club_clubid_index(request, club_id):
    club = ''
    # 根据id获取的社团
    template = loader.get_template('club/clubid/index.html')
    content = {'club': club}
    return HttpResponse(template.render(content, request))


def club_clubid_posts(request, club_id):
    posts = ''
    # 根据id获取该社团所有动态(匹配一下作者）
    template = loader.get_template('club/clubid/posts.html')
    content = {'posts': posts}
    return HttpResponse(template.render(content, request))


def club_clubid_post(request, post_id):
    post = ''
    # 根据id获取一篇动态
    template = loader.get_template('club/clubid/post.html')
    content = {'post': post}
    return HttpResponse(template.render(content, request))


def club_admin_login(request):
    template = loader.get_template('')
    content = {}
    return HttpResponse(template.render(content, request))


# test
def wto_test(request):
    template = loader.get_template('admin/base.html')
    content = {}
    return HttpResponse(template.render(content, request))


def test(request):
    template = loader.get_template('')
    content = {}
    return HttpResponse(template.render(content, request))

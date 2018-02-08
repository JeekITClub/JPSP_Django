# coding=utf-8
from django.http import HttpResponse, HttpResponseServerError
import json
from django.template import loader
from django.contrib.auth.models import User
from jpspapp.models import Club, Post, Activity, Classroom, LostAndFound, UserProfile, CDUser, ActivityParticipantShip, \
    ClubMemberShip
from django.views.decorators.http import require_http_methods
import datetime
from django.contrib.auth import authenticate
from django.core.paginator import Paginator


# Create your views here.


@require_http_methods(['GET'])
def index(request):
    if request.user.is_authenticated:
        try:
            template = loader.get_template('index/index.html')
            content = {}
            return HttpResponse(template.render(content, request))
        except:
            return HttpResponseServerError
    else:
        try:
            template = loader.get_template('index/index.html')
            content = {}
            return HttpResponse(template.render(content, request))
        except:
            return HttpResponseServerError


@require_http_methods(['GET'])
def login_page(request):
    template = loader.get_template('index/login.html')
    content = {}
    return HttpResponse(template.render(content, request))


def admin_login_page(request):
    template = loader.get_template('manage/login.html')
    content = {}
    return HttpResponse(template.render(content, request))


@require_http_methods(['POST'])
def login(request):
    try:
        user_id = request.POST['UserName']
        password = request.POST['Password']
        user = authenticate(username=user_id, password=password)
        return HttpRedirect()
    except:
        return HttpResponse("Login Error")


@require_http_methods(['POST'])
def logout(request):
    pass

@require_http_methods(['POST'])
def club_establish(request):
    if request.user.is_authenticated:
        try:
            clubname = request.POST['Clubname']
            shezhang_name = request.POST['Shezhang_Name']
            shezhang_qq = request.POST['Shezhang_QQ']
            shezhang_grade = request.POST['Shezhang_Grade']
            shezhang_classroom = request.POST['Shezhang_Classroom']
            introduction = request.POST['Introduction']
            if_recruit = request.POST['IfRecruit']
            qq_group = request.POST['QQGroup']
            email = request.POST['Email']
            Club.objects.create(
                Clubname=clubname,
                # TODO: ClubId
                ShezhangName=shezhang_name,
                SheZhangQq=shezhang_qq,
                ShezhangGrade=shezhang_grade,
                ShezhangClassroom=shezhang_classroom,
                IfRecruit=if_recruit,
                Introduction=introduction,
                Email=email,
                # TODO: label!
                State=False,
                Achievements="",
                Stars=0,
                EnrollGroupQq=qq_group,
            )
            return HttpResponse("Success")
        except:
            return HttpResponseServerError
    else:
        return HttpResponse("没登陆呢")


# 社团部访问接口
@require_http_methods(['POST'])
def club_list(request):
    if request.user.is_authenticated:

        try:
            body = json.loads(request.body)
            user_id = body['UserId']
            type = body['Type']

        except:
            return HttpResponseServerError
    else:
        return HttpResponse("没登陆呢")


# 学生 社团列表
# Fix the unordered problem
# Fixed by add class Meta to the model Club 2018-02-08 2:26PM by Harvey Qiu
def student_club_list(request, page):
    club_object = Club.objects.filter(State=True)
    paginator = Paginator(club_object, 1)
    # paginator is a new Paginator
    template = loader.get_template('index/club/list.html')
    return HttpResponse(template.render({'club_list':paginator.get_page(page)}, request))


def student_club_establish(request):
    context = {}
    template = loader.get_template('index/club/establish.html')
    return HttpResponse(template.render(context, request))


@require_http_methods(['POST'])
def club_attend(request):
    if request.user.is_authenticated:
        try:
            user_id = request.POST['UserId']
            club_id = request.POST['ClubId']
        except:
            return False
    else:
        return HttpResponse("Attend the club Error")


@require_http_methods(['POST'])
def club_quit(request):
    if request.user.is_authenticated:
        try:
            user_id = request.POST['UserId']
            club_id = request.POST['ClubId']
        except:
            return False
    else:
        return HttpResponse("Quit the club Error")


@require_http_methods(['GET'])
def club_member(request):
    if request.user.is_authenticated:
        try:
            template = loader.get_template('club/member/list.html')
            content = {}
            return HttpResponse(template.render(content, request))
        except:
            return HttpResponseServerError
    else:
        return HttpResponse("未登陆")


# @require_http_methods(['POST'])
# def club_member_add(request):
#     if request.user.is_authenticated:
#         try:
#             body = json.loads(request.body)
#             # club_id -> example: '303'
#             club_id = request.POST['ClubId']
#             # username -> example: 'S320150181'
#             username = request.body['UserName']
#
#             ClubMemberShip.objects.create(
#                 Member=UserProfile.objects.get(UserObject=User.objects.get(username=username)),
#                 Club=Club.objects.get(ClubId=club_id))
#
#         except:
#             return HttpResponseServerError
#     else:
#         return HttpResponse("未登陆")

# @require_http_methods(['POST'])
# def club_confirmed_member_list(request):
#     try:
#         # TODO: how to identify confirmed and unconfirmed
#         body = json.loads(request.body)
#         token = body['Token']
#         page = body['Page']
#         # club_id -> example: '303'
#         club_id = body['ClubId']
#         if (token_authenticate(user_id=club_id, token=token)):
#             membership_set = ClubMemberShip.objects.filter(Club=Club.objects.get(ClubId=club_id)).filter(State=1)
#             response = []
#             paginator = Paginator(membership_set, 10)
#             membership_set_page = paginator.page(page)
#             for membership in membership_set_page:
#                 response.append({
#                     'UserName': membership.Member.UserName,
#                     'Class': membership.Member.Class,
#                     'Grade': membership.Member.Grade,
#                     'AttendYear': membership.Member.AttendYear,
#                     'Phone': membership.Member.Phone,
#                     'QQ': membership.Member.QQ
#                 })
#             response_json = json.dumps(response)
#             return JsonResponse({
#                 'message': 'success',
#                 'Access-Control-Allow-Origin': '*',
#                 'data': response_json
#             }, safe=False)
#         else:
#             return JsonResponse({
#                 'message': 'error',
#                 'Access-Control-Allow-Origin': '*'
#             })
#     except:
#         return JsonResponse({
#             'message': 'error',
#             'Access-Control-Allow-Origin': '*'
#         })


# @require_http_methods(['POST'])
# def club_unconfirmed_member_list(request):
#     try:
#         body = json.loads(request.body)
#         token = body['Token']
#         # club_id -> example: '303'
#         page = body['Page']
#         club_id = body['ClubId']
#         if (token_authenticate(user_id=club_id, token=token)):
#             membership_set = ClubMemberShip.objects.filter(Club=Club.objects.get(ClubId=club_id)).filter(State=0)
#             response = []
#             paginator = Paginator(membership_set, 10)
#             membership_set_page = paginator.page(page)
#             for membership in membership_set_page:
#                 response.append({
#                     'UserName': membership.Member.UserName,
#                     'Class': membership.Member.Class,
#                     'Grade': membership.Member.Grade,
#                     'AttendYear': membership.Member.AttendYear,
#                     'Phone': membership.Member.Phone,
#                     'QQ': membership.Member.QQ
#                 })
#             response_json = json.dumps(response)
#             return JsonResponse({
#                 'message': 'success',
#                 'Access-Control-Allow-Origin': '*',
#                 'data': response_json
#             }, safe=False)
#         else:
#             return JsonResponse({
#                 'message': 'error',
#                 'Access-Control-Allow-Origin': '*'
#             })
#
#     except:
#         return JsonResponse({
#             'message': 'error',
#             'Access-Control-Allow-Origin': '*'
#         })


# @require_http_methods(['POST'])
# def recruit_classroom_apply(request):
#     try:
#         body = json.loads(request.body)
#         token = body['Token']
#         club_id = body['ClubId']
#         club_name = body['ClubName']
#         date1 = body['Date1']
#         date2 = body['Date2']
#         # TODO: deal with date
#         Classroom.objects.create(
#             ClassroomId=0,
#             ClubId=Club.objects.get(User.objects.get(username=club_id)),
#             ClubName=club_name,
#             Date1=date1,
#             Date2=date2
#         )
#         return JsonResponse({
#             'message': 'success',
#             'Access-Control-Allow-Origin': '*'
#         })
#     except:
#         return JsonResponse({
#             'message': 'error',
#             'Access-Control-Allow-Origin': '*'
#         })


# @require_http_methods(['POST'])
# def recruit_classroom_operate(request):
#     try:
#         body = json.loads(request.body)
#         token = body['Token']
#         classroom = body['Classroom']
#         clubid = body['ClubId']
#         # date
#         return JsonResponse({
#             'message': 'error',
#             'Access-Control-Allow-Origin': '*'
#         })
#     except:
#         return JsonResponse({
#             'message': 'error',
#             'Access-Control-Allow-Origin': '*'
#         })


# @require_http_methods(['POST'])
# def recruit_classroom_list(request):
#     try:
#         body = json.loads(request.body)
#         token = body['Token']
#         type = body['Type']
#         response = []
#         if type == 'Confirmed':
#             pass
#         elif type == 'Denied':
#             pass
#         elif type == 'Unconfirmed':
#             pass
#         elif type == 'All':
#             classroom_objects_set = Classroom.objects.all()
#             # TODO: !!!!!!!
#             for classroom in classroom_objects_set:
#                 response.append({})
#         response_json = json.dumps(response)
#     except:
#         return 0

# @require_http_methods(['POST'])
# def club_member_remove(request):
#     try:
#         body = json.loads(request.body)
#         token = body['token']
#         # club_id -> example: '303'
#         club_id = body['ClubId']
#         # username -> example: 'S320150181'
#         user_id = body['UserId']
#         if (token_authenticate(user_id=club_id, token=token)):
#             ClubMemberShip.objects.get(Club=Club.objects.get(ClubId=club_id), Member=UserProfile.objects.get(
#                 UserObject=User.objects.get(username=user_id))).delete()
#             return JsonResponse({
#                 'message': 'success',
#                 'Access-Control-Allow-Origin': '*'
#             })
#         else:
#             return JsonResponse({
#                 'message': 'error',
#                 'Access-Control-Allow-Origin': '*'
#             })
#
#     except:
#         return JsonResponse({
#             'message': 'error',
#             'Access-Control-Allow-Origin': '*'
#         })


# @require_http_methods(['POST'])
# def activity_apply(request):
#     try:
#         body = json.loads(request.body)
#         token = body['Token']
#         club_id = body['ClubId']
#         activity_name = body['Name']
#         region = body['Region']
#         date1 = body['Date1']
#         date2 = body['Date2']
#         content = body['Content']
#         type = body['Type']
#         Activity.objects.create(
#             ActivityName=activity_name,
#             Region=region,
#             Clubid=Club.objects.get(clubid=User.objects.get(username=club_id)),
#             ClubName=Club.objects.get(clubid=User.objects.get(username=club_id)).ClubName,
#             Content=content,
#             Date1=date1,
#             Date2=date2,
#             State='0',
#             Type=type
#         )
#         return JsonResponse({
#             'message': 'success',
#             'Access-Control-Allow-Origin': '*'
#         })
#     except:
#         return JsonResponse({
#             'message': 'error',
#             'Access-Control-Allow-Origin': '*'
#         })


# @require_http_methods(['POST'])
# def activity_attend(requset):
#     try:
#         body = json.loads(requset.body)
#
#         # token = body['Token']
#         # activity_id -> int
#         activity_id = body['ActivityId']
#         # user_id -> str
#         user_id = body['UserId']
#         ActivityParticipantShip.objects.create(Activity=Activity.objects.get(pk=activity_id),
#                                                Participant=UserProfile.objects.get(
#                                                    UserObject=User.objects.get(username=user_id)))
#         return JsonResponse({
#             'message': 'success',
#             'Access-Control-Allow-Origin': '*'
#         })
#     except:
#         return JsonResponse({
#             'message': 'error',
#             'Access-Control-Allow-Origin': '*'
#         })


# @require_http_methods(['POST'])
# def activity_detail(request):
#     try:
#         body = json.loads(request.body)
#         # activity_id -> int
#         activity_id = body['ActivityId']
#         activity = Activity.objects.get(pk=1)
#         return JsonResponse({
#             'message': 'success',
#             'Access-Control-Allow-Origin': '*',
#             'data': {
#                 'Name': activity.Name,
#                 'Region': activity.Region,
#                 'ClubName': activity.ClubObject.ClubName,
#                 'Content': activity.Content,
#                 'Date1': str(activity.Date1),
#                 'Date2': str(activity.Date2),
#             }
#         })
#     except:
#         return JsonResponse({
#             'message': 'error',
#             'Access-Control-Allow-Origin': '*'
#         })


# @require_http_methods(['POST'])
# def activity_operate(request):
#     try:
#         body = json.loads(request.body)
#         token = body['token']
#         activity_id = body['ActivityId']
#         operation = body['Operation']
#         if operation == 'Confirm':
#             try:
#                 activity_object = Activity.objects.get(pk=activity_id)
#                 activity_object.State = 'Confirmed'
#                 activity_object.save()
#                 return JsonResponse({
#                     'message': 'success',
#                     'Access-Control-Allow-Origin': '*'
#                 })
#             except:
#                 return JsonResponse({
#                     'message': 'error',
#                     'Access-Control-Allow-Origin': '*'
#                 })
#         elif operation == 'UndoDeny':
#             try:
#                 activity_object = Activity.objects.get(pk=activity_id)
#                 activity_object.State = 'Unconfirmed'
#                 activity_object.save()
#             except:
#                 return JsonResponse({
#                     'message': 'error',
#                     'Access-Control-Allow-Origin': '*'
#                 })
#         elif operation == 'Deny':
#             try:
#                 activity_object = Activity.objects.get(pk=activity_id)
#                 activity_object.State = 'Denied'
#                 activity_object.save()
#             except:
#                 return JsonResponse({
#                     'message': 'error',
#                     'Access-Control-Allow-Origin': '*'
#                 })
#     except:
#         return JsonResponse({
#             'message': 'error',
#             'Access-Control-Allow-Origin': '*'
#         })


# @require_http_methods(['POST'])
# def activity_list(request):
#     try:
#         body = json.loads(request.body)
#         token = body['Token']
#         type = body['Type']
#         response = []
#         activityList = None
#         if type == 'All':
#             activityList = Activity.objects.all()
#         elif type == 'Past':
#             activityList = Activity.objects.filter(Date2__lt=datetime.datetime.now())
#         elif type == 'Happening':
#             activityList = Activity.objects.filter(Date1__lte=datetime.datetime.now()).filter(
#                 Date2__gte=datetime.datetime.now())
#         elif type == 'Future':
#             activityList = Activity.objects.filter(Date1__gt=datetime.datetime.now())
#         elif type == 'Unconfirmed':
#             activityList = Activity.objects.filter(State='0')
#         elif type == 'Confirmed':
#             activityList = Activity.objects.filter(State='1')
#         elif type == 'Denied':
#             activityList = Activity.objects.filter(State='2')
#         # TODO : token authenticate
#         for data in activityList:
#             response.append({
#                 'ActivityId': data.pk,
#                 'Name': data.Name,
#                 'Region': data.Region,
#                 # 'ClubId': data.ClubId,
#                 'ClubName': data.ClubName,
#                 'Content': data.Content,
#                 'Date1': str(data.Date1),
#                 'Date2': str(data.Date2),
#                 'State': data.State,
#                 'Type': data.Type
#             })
#         response_json = json.dumps(response)
#         return JsonResponse({'message': 'success', 'Access-Control-Allow-Origin': '*', 'data': response_json},
#                             safe=False)
#     except:
#         return JsonResponse({
#             'message': 'error',
#             'Access-Control-Allow-Origin': '*'
#         })


# @require_http_methods(["POST"])
# def laf_submit(request):
#     try:
#         body = json.loads(request.body)
#         token = body['Token']
#         lostOrFound = body['LostOrFound']
#         objectName = body['ObjectName']
#         linkmanName = body['LinkmanName']
#         linkmanGrade = body['LinkmanGrade']
#         linkmanPhoneNumber = body['LinkmanPhoneNumber']
#         linkmanClass = body['LinkmanClass']
#         linkmanQq = body['LinkmanQq']
#         region = body['Region']
#         date1 = body['Date1']
#         importance = body['Importance']
#         desc = body['Desc']
#         try:
#             LostAndFound.objects.create(
#                 LostOrFound=lostOrFound,
#                 LinkmanName=linkmanName,
#                 LinkmanGrade=linkmanGrade,
#                 LinkmanClassroom=linkmanClass,
#                 LinkmanPhoneNumber=linkmanPhoneNumber,
#                 LinkmanQq=linkmanQq,
#                 LostObjectName=objectName,
#                 LostPlace=region,
#                 Importance=importance,
#                 Desc=desc,
#                 LostDateTime=date1
#             )
#             return JsonResponse({
#                 'message': 'error',
#                 'Access-Control-Allow-Origin': '*'
#             })
#         except:
#             return JsonResponse({
#                 'message': 'error',
#                 'Access-Control-Allow-Origin': '*'
#             })
#     except:
#         return JsonResponse({
#             'message': 'error',
#             'Access-Control-Allow-Origin': '*'
#         })


# @require_http_methods(["POST"])
# def laf_list(request):
#     try:
#         body = json.loads(request.body)
#         type = body['Type']
#         response = []
#         LostAndFoundList = None
#         if type == 'Lost':
#             LostAndFoundList = LostAndFound.objects.filter()
#             # TODO: filter
#         elif type == 'Found':
#             LostAndFoundList = LostAndFound.objects.all()
#             # TODO: filter
#         elif type == 'Past':
#             LostAndFoundList = LostAndFound.objects.all()
#             # TODO: filter
#         elif type == 'All':
#             LostAndFoundList = LostAndFound.objects.all()
#         for data in LostAndFoundList:
#             response.append({
#                 'LostorFound': data.LostOrFound,
#                 'ObjectName': data.LostObjectName,
#                 'LinkmanGrade': data.LinkmanGrade,
#                 'LinkmanClass': data.LinkmanClass,
#                 'LinkmanPhoneNumber': data.LinkmanPhoneNumber,
#                 'LinkmanQq': data.LinkmanQq,
#                 'LinkmanName': data.LinkmanName,
#                 'Region': data.LostPlace,
#                 'Date1': data.LostDateTime,
#                 'Importance': data.Importacne,
#                 'Desc': data.Desc
#             })
#         response_json = json.dumps(response)
#         return JsonResponse({'message': 'success', 'Access-Control-Allow-Origin': '*', 'data': response_json},
#                             safe=False)
#     except:
#         return JsonResponse({
#             'message': 'error',
#             'Access-Control-Allow-Origin': '*'
#         })


def student_club_detail(request, club_id):
    profile = Club.objects.get(ClubId=club_id)
    template = loader.get_template('index/club/detail.html')
    content = {}
    return HttpResponse(template.render(content, request))


def student_club_news(request, club_id):
    # todo: finish the function
    profile = Club.objects.get(ClubId=club_id)
    template = loader.get_template('index/club/detail.html')
    content = {}
    return HttpResponse(template.render(content, request))


@require_http_methods(["POST"])
def club_profile_update(request):
    body = request.POST
    shezhang_name = body['shezhang_name']
    shezhang_qq = body['shezhang_qq']
    shezhang_grade = body['shezhang_grade']
    shezhang_class = body['shezhang_class']
    if_recruit = body['if_recruit']
    enroll_group_qq = body['enroll_group_qq']
    email = body['email']
    label = body['label']
    state = body['state']
    introduction = body['introduction']
    achievements = body['achievements']
    club_object = Club.objects.get(ClubId=body['clubid'])
    club_object.ClubName = body['clubname']
    club_object.ShezhangName = shezhang_name
    club_object.ShezhangGrade = shezhang_grade
    club_object.ShezhangClassroom = shezhang_class
    club_object.ShezhangQq = shezhang_qq
    club_object.IfRecruit = if_recruit
    club_object.EnrollGroupQq = enroll_group_qq
    club_object.Email = email
    club_object.Label = label
    club_object.State = state
    club_object.Introduction = introduction
    club_object.Achievements = achievements
    club_object.save()


@require_http_methods(["POST"])
def event_submit(request):
    pass


@require_http_methods(["POST"])
def event_list(request):
    template = loader.get_template('admin/event/list.html')
    content = {}
    return HttpResponse(template.render(content, request))


def admin_file_upload(request):
    template = loader.get_template('admin/file/upload.html')
    content = {}
    return HttpResponse(template.render(content, request))


def admin_file_upload_list(request):
    template = loader.get_template('admin/file/upload_list.html')
    content = {}
    return HttpResponse(template.render(content, request))


def admin_file_download_list(request):
    template = loader.get_template('admin/file/download_list.html')
    content = {}
    return HttpResponse(template.render(content, request))


def club_file_upload(request):
    template = loader.get_template('club/file/upload.html')
    content = {}
    return HttpResponse(template.render(content, request))


def club_file_upload_list(request):
    template = loader.get_template('club/file/upload_list.html')
    content = {}
    return HttpResponse(template.render(content, request))


@require_http_methods(['POST'])
def club_file_download_list(request):
    template = loader.get_template('club/file/download_list.html')
    content = {}
    return HttpResponse(template.render(content, request))


def student_dashboard_index(request):
    if request.user.is_authenticated:
        try:
            template = loader.get_template('index/dashboard/index.html')
            content = {}
            return HttpResponse(template.render(content, request))
        except:
            return HttpResponseServerError
    else:
        # todo: redirect to the login page
        return HttpResponse("0")


def student_dashboard_clubs(request):
    if request.user.is_authenticated:
        template = loader.get_template('index/dashboard/clubs.html')
        content = {}
        return HttpResponse(template.render(content, request))
    else:
        # todo: redirect to the login page
        return HttpResponse("0")


def student_dashboard_activities(request):
    if request.user.is_authenticated:
        template = loader.get_template('index/dashboard/activities.html')
        content = {}
        return HttpResponse(template.render(content, request))
    else:
        # todo: redirect to the login page
        return HttpResponse("0")


def student_dashboard_password(request):
    if request.user.is_authenticated:
        try:
            template = loader.get_template('index/dashboard/password.html')
            content = {}
            return HttpResponse(template.render(content, request))
        except:
            return HttpResponseServerError
    else:
        # todo: redirect to the login page
        return HttpResponse("0")


# todo: write a decorator for admin
def admin_student_list(request):
    if request.user.is_authenticated:
        template = loader.get_template('admin/student/list.html')
        content = {}
        return HttpResponse(template.render(content, request))
    else:
        # todo: redirect to the login page
        return HttpResponse("0")


def admin_student_detail(request):
    template = loader.get_template('admin/student/detail.html')
    content = {}
    return HttpResponse(template.render(content, request))

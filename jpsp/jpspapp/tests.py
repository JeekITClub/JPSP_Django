from django.test import TestCase, Client
from jpspapp.models import Club, Activity,UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import datetime


# Create your tests here.

class ClubTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="clubtest", email='123@123.com', password='jp123456')
        Club.objects.create(ClubObject=User.objects.get(username='clubtest'), ClubName="测试社团", ClubId=601, Type='1',
                            ShezhangName="社长", ShezhangQq="12345678", ShezhangGrade='1', ShezhangClass='1',
                            IfRecruit=True, EnrollGroupQq='12345678')

    def test_club_update(self):
        club = Club.objects.get(ClubName="测试社团")
        club.ShezhangName = "社长姓名"
        club.save()
        self.assertEqual(club.ShezhangName, "社长姓名")

    def test_club_del(selfs):
        club = Club.objects.get(ClubName="测试社团")
        club.delete()
        user = User.objects.get(username="clubtest")
        user.delete()


class ActivityModelTest(TestCase):
    def setUp(self):
        User.objects.create_user(username="clubtest", email='123@123.com', password='jp123456')
        Club.objects.create(ClubObject=User.objects.get(username='clubtest'), ClubName="测试社团", ClubId=601, Type='1',
                            ShezhangName="社长", ShezhangQq="12345678", ShezhangGrade='1', ShezhangClass='1',
                            IfRecruit=True, EnrollGroupQq='12345678')
        Activity.objects.create(Name="活动名称", Region="活动地点", ClubObject=Club.objects.get(ClubName="测试社团"),
                                Content="活动内容", Date1=datetime.datetime.now(),
                                Date2=datetime.datetime.now() + datetime.timedelta(days=1), State='0', Type='普通')

    def test_update(self):
        activity = Activity.objects.get(Name="活动名称")
        activity.Content = "活动内容测试"
        activity.save()
        self.assertEqual(activity.Content, '活动内容测试')

    def test_delete(self):
        Activity.objects.get(Region="活动地点").delete()
        Club.objects.get(ShezhangName='社长').delete()
        User.objects.get(username='clubtest').delete()


class UserProfileModelTest(TestCase):
    def setUp(self):
        User.objects.create(username='userprofiletest',email='123@123.com',password='jp123456')
        UserProfile.objects.create(UserObject=User.objects.get(username='userprofiletest'),UserName='测试用户',Class=1,Grade=1,AttendYear='2017',QQ='12345678',Phone='12345678901',Email='123@123.com')


    def test_update(self):
        user = UserProfile.objects.get(UserName='测试用户')
        user.Class= 2
        user.save()
        self.assertEqual(user.Class,2)

    def test_delete(self):
        user = UserProfile.objects.get(UserName='测试用户')
        user.delete()


class UserModelTest(TestCase):
    def create(self):
        pass

    def update(selfs):
        pass

    def delete(self):
        pass


class PostModelTest(TestCase):
    def test(self):
        pass

    def update(selfs):
        pass

    def delete(self):
        pass


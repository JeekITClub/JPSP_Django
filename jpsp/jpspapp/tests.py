from django.test import TestCase, Client
from jpspapp.models import Token, Club
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your tests here.

class ClubTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='clubtest', email='123@123.com', password='jp123456')
        Club.objects.create(ClubObject=User.objects.get(username='clubtest'), ClubName="测试社团", ClubId=601, Type='1',
                            ShezhangName="社长", ShezhangQq="12345678", ShezhangGrade='1', ShezhangClass='1',
                            IfRecruit=True, EnrollGroupQq='12345678')

    def test_club_update(self):
        club = Club.objects.get(ClubName="测试社团")
        club.ShezhangName = "社长姓名"
        club.save()
        self.assertEqual(club.ShezhangName,"社长姓名")

    def test_club_del(selfs):
        club = Club.objects.get(ClubName="测试社团")
        club.delete()

class ActivityModelTest(TestCase):
    def setUp(self):
        pass

    def update(selfs):
        pass

    def delete(self):
        pass


class UserProfileModelTest(TestCase):
    def create(self):
        pass

    def update(selfs):
        pass

    def delete(self):
        pass


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

from django.test import TestCase, Client
from jpspapp.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your tests here.

class ClubModelTest(TestCase):
    def create(self):
        pass

    def update(selfs):
        pass

    def delete(self):
        pass


class ActivityModelTest(TestCase):
    def create(self):
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
    def create(self):
        pass

    def update(selfs):
        pass

    def delete(self):
        pass


class LogTest(TestCase):
    # 登入、登出测试
    def login(self):
        # c = Client()
        pass

    def logout(self):
        pass


class PostOperationTest(TestCase):
    def submit(self):
        pass

    def list(self):
        pass

    def confirm(self):
        pass

    def deny(self):
        pass

    def undo(self):
        pass


class ActivityOperationTest(TestCase):
    def apply(self):
        pass

    def list(self):
        pass

    def attend(self):
        pass

    def cancel(self):
        pass

    def confirm(self):
        pass

    def deny(self):
        pass

    def undo(self):
        pass

    def undo_attend(self):
        pass

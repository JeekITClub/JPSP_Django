# JPSP Shortcut
# Created by WTO on 2017/5/28 19:25
from jpspapp.models import Token
from django.contrib.auth.models import User
import random
import datetime

alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"


class JPSPToken:
    def __init__(self, username, usertype, token=""):
        self.token = ""
        if token != "":
            self.token = token
        else:
            pass
        self.username = username
        self.usertype = usertype
        self.message = ''

    def generate(self, length=30):
        for i in range(length):
            self.token += alphabet[random.randint(0, len(alphabet) - 1)]
        try:
            Token.objects.create(
                Token=self.token,
                User=User.objects.get(username=self.username),
                UserType=self.usertype
                # start_time=datetime.datetime.now(),
                # TODO:  datetime in python and SQL ??
                # end_time =datetime.datetime.now(),
            )
            self.message = 'Message'
            return self.token
        except:
            self.message = 'error'

    def remove(self):
        try:
            token = Token.objects.get(UserName=self.username, UserType=self.usertype)
            if token:
                token.delete()
        except:
            return False

    def authenticate(self):
        token = Token.objects.get(UserName=self.username, UserType=self.usertype).Token
        if token:
            if self.token == token:
                return True
            else:
                return False


class JPSPTime:
    def __init__(self):
        pass

    def compare(self):
        pass

    def add(self, date1, date2):
        pass

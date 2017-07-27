# JPSP Shortcut
# Created by WTO on 2017/5/28 19:25
from jpspapp.models import Token
from django.contrib.auth.models import User
import random
import datetime

alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"


class JPSPToken:
    def __init__(self, username, token=""):
        self.token = ""
        if token != "":
            self.token = token
        else:
            pass
        self.username = username
        self.message = ''

    def generate(self, length=30):
        for i in range(length):
            self.token += alphabet[random.randint(0, len(alphabet) - 1)]
        try:
            Token.objects.create(
                Token=self.token,
                UserName=self.username
            )
        except:
            token_object = Token.objects.get(UserName=self.username)
            token_object.Token = self.token
            token_object.save()
        finally:
            return self.token

    def remove(self):
        try:
            token = Token.objects.get(UserName=self.username)
            if token:
                token.delete()
        except:
            return False

    def authenticate(self):
        token = Token.objects.get(UserName=self.username).Token
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

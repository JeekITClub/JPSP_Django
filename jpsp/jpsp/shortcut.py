# JPSP Shortcut
# Created by WTO on 2017/5/28 19:25
from jpspapp.models import Token
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

    def generate(self, length=30):
        for i in range(length):
            self.token += alphabet[random.randint(0, len(alphabet) - 1)]
        Token.objects.create(
            token=self.token,
            user=self.username,
            usertype=self.usertype,
            start_time=datetime.datetime.now(),
            # TODO: end time problem
            # end_time =datetime.datetime.now(),
        )
        return self.token

    def remove(self):
        token = Token.objects.filter(username=self.username)
        if token:
            token.delete()

    def authenticate(self):
        token = Token.objects.filter(username=self.username)
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

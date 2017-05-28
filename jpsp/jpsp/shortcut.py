# JPSP Shortcut
# Created by WTO on 2017/5/28 19:25
from jpspapp.models import Token
import random
import datetime

alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"


class Token:
    def __init__(self, username, usertype):
        self.token = ""
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

    def remove(self, username):
        token = Token.objects.filter(user=username)
        if token:
            token.delete()


class JPSPTime:
    def __init__(self):
        pass

    def compare(self):
        pass

    def add(self, date1, date2):
        pass

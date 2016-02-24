from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
import hashlib
# Create your models here.

@python_2_unicode_compatible
class Message(models.Model):
    title = models.CharField(max_length=20)
    message = models.CharField(max_length=255,default='')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_msg_body(self):
        return self.body


class Secret_Message(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    message = models.CharField(max_length=255,default='')
    def __str__(self):
        return self.srt_title

    def get_srt_msg(self):
        return self.srt_msg_body

def get_knock_url(num):
    if num == 0:
        return '/user/register/'
    elif num == 1:
        return '/user/login/'
    elif num == 2:
        return '/message/add/'
    elif num == 3:
        return '/message/list/'

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    secret = models.BooleanField(default = False)
    knock_position = models.IntegerField(default = 0)
    knock_url_0 = models.CharField(max_length = 20,default = '')
    knock_url_1 = models.CharField(max_length = 20,default = '')
    knock_url_2 = models.CharField(max_length = 20,default = '')
    knock_url_3 = models.CharField(max_length = 20,default = '')

    def __str__(self):
        return self.user.username


    def getHash(self):
        m = hashlib.md5()
        name = str(self)
        m.update(name)
        s = m.hexdigest()
        self.knock_url_0 = get_knock_url(int(s[0],base=16) % 4) 
        self.knock_url_1 = get_knock_url(int(s[1],base=16) % 4) 
        self.knock_url_2 = get_knock_url(int(s[2],base=16) % 4) 
        self.knock_url_3 = get_knock_url(int(s[3],base=16) % 4) 
        return self



from django.db import models
from django.utils import timezone
import datetime
import httplib
import urlparse

# Create your models here.
class Dump(models.Model):
  LINK = 'L'
  POST = 'B'
  PICTURE = 'P'
  DUMP_TYPES = (
    (LINK, 'Link'),
    (POST, 'Post'),
    (PICTURE, 'Picture'),
  )

  type = models.CharField(max_length=2, choices=DUMP_TYPES, default=POST)
  title = models.CharField(max_length=128)
  description = models.TextField(blank=True)
  follow_up = models.BooleanField(default=False)
  date = models.DateTimeField(default=timezone.now())

  def __unicode__(self):
    return self.type + u"'" + self.title + u"'"

  def was_posted_recently(self):
    return self.date >= timezone.now() - datetime.timedelta(days=1)

class Link(models.Model):

  PICTURE_TYPES = ['jpeg', 'jpg', 'gif', 'png']

  dump = models.ForeignKey(Dump)
  url = models.URLField()

  def __unicode__(self):
    return self.url

  def is_a_picture(self):
    if "." in self.url:
      extension = self.url.split(".")[-1]
      for picture_type in self.PICTURE_TYPES:
        if extension == picture_type:
          return True
      
    return False

  def url_is_valid(self):
    VALID_RESPONSES = [200, 301, 302]
    valid = False;

    host, path = urlparse.urlsplit(self.url)[1:3]
    try:
      connection = httplib.HTTPConnection(host)
      connection.request("HEAD", path)
      responseObject = connection.getresponse()
      if responseObject.status in VALID_RESPONSES:
        valid = True
    except:
      pass

    return valid

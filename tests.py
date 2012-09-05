"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from brain_dump.models import Dump, Link

class LinkTestCase(TestCase):

  def test_creation(self):
    my_url = 'http://awesome.url.com'
    link = Link(url=my_url)
    self.assertEqual(my_url, link.url) 

  def test_is_a_picture(self):
    PICTURES = [
      'test.jpeg',
      'hello.jpg',
      'avatar.png',
      'animated.gif',
    ]
      
    for picture in PICTURES:
      my_url = "http://localhost/" + picture
      link = Link(url=my_url)
      self.assertTrue(link.is_a_picture())

    NOT_PICTURES = [
      'text.txt',
      'hello',
      'goodbye/',
      'this.is.a.sentence',
    ]
    
    for not_picture in NOT_PICTURES:
      my_url = "http://localhost/" + not_picture
      link = Link(url=my_url)
      self.assertFalse(link.is_a_picture())

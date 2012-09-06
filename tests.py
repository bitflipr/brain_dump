"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from brain_dump.models import Dump, Link
from django.db import DatabaseError

class DumpTestCase(TestCase):
  
  def dump_creation(self):
    my_type = 'L'
    my_title = 'Title'
    my_description = 'Description'
    my_follow_up = True
    my_date = timezone.now()

    dump = Dump(type=my_type, title=my_title, description=my_description, follow_up=my_follow_up, date=my_date)

    self.assertEqual(my_type, dump.type)
    self.assertEqual(my_title, dump.title)
    self.assertEqual(my_description, dump.description)
    self.assertEqual(my_follow_up, dump.follow_up)
    self.assertEqual(my_date, dump.date)

class LinkTestCase(TestCase):

  def test_creation(self):
    my_url = 'http://awesome.url.com'
    link = Link(url=my_url)
    self.assertEqual(my_url, link.url) 

  def test_url_is_valid(self):
    VALID_URLS = [
      'http://www.google.com',
      'http://www.microsoft.com/windows',
    ]
    
    for my_url in VALID_URLS:
      link = Link(url=my_url)
      self.assertTrue(link.url_is_valid(), msg='[%s] is an invalid url' % link)

    INVALID_URLS = [
      'this_is_not_an_url',
      'http://www.asldkfjsaldkjfldsakjf.com',
    ]
    
    for my_url in INVALID_URLS:
      link = Link(url=my_url)
      self.assertFalse(link.url_is_valid(), msg='[%s] is a valid url' % link)

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

class DumpWithLinksTestCase(TestCase):

  def test_link_set_in_dump(self):
    my_title = 'Simple Dump'
    dump = Dump(title=my_title)
    dump.save()
    link = dump.link_set.create(url='http://localhost')
    link.save()

    self.assertIsInstance(link, Link)
    self.assertEqual(dump.link_set.all()[0], link)
    self.assertEqual(link.dump.title, my_title)

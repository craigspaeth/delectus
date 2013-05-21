"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""
from django.test import TestCase
from delectus.models import Tape

class TapeTest(TestCase):

	def test_as_unicode_shows_title(self):
		"""
		__unicode__ should print out the title of the tape.
		"""
		tape = Tape(title= 'Beauty Plus Pity')
		self.assertEqual(Tape.__unicode__(tape), 'Beauty Plus Pity')
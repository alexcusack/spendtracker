from django.test import TestCase
from ..extractEmailContents import *
import json

class ExtractEmailContentsTestCase(TestCase):

	def setup(self):
		None


	def test_getCurrentChargeAmount(self):
		"""Should correctly extract the dollar amount from a string"""
		sampleInput = json.load(open('spendTrackerApp/tests/fixtures/sample-chase-payload.json'))
					
		input = {
			'FromName': 'TestCase',
			'TextBody': sampleInput.get('TextBody')
		}
		self.assertEqual(getCurrentChargeAmount(input), 1129)


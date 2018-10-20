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

	def test_tokenizeFromCloudMail(self):
		sampleInput = json.load(open('spendTrackerApp/tests/fixtures/cloudmail-sample-body.json'))
		input = {
			'plain': sampleInput.get('plain')
		}
		self.assertEqual(tokenizeFromCloudMail(input), {
			'charge_amount': 1299,
			'vendor_name': 'apl*itunes.com/bill'
		})


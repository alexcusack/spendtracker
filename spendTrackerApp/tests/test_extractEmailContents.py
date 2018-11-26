from django.test import TestCase
from ..extractEmailContents import *
import json

class ExtractEmailContentsTestCase(TestCase):

	def setup(self):
		None

	def test_tokenizeFromCloudMail(self):
		sampleInput = json.load(open('spendTrackerApp/tests/fixtures/cloudmail-sample-body.json'))
		input = {
			'envelope': sampleInput.get('envelope'),
			'headers': sampleInput.get('headers'),
			'plain': sampleInput.get('plain')
		}
		self.assertEqual(tokenizeFromCloudMail(input), {
			'to': '6164431505',
			'charge_amount': 1299,
			'vendor_name': 'apl*itunes.com/bill', 
			'subject': 'your single transaction alert from chase'
		})


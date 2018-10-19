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


	def test_shoudWorkForCloudMailFormat(self):
		sampleInput = json.load(open('spendTrackerApp/tests/fixtures/cloudmail-sample-body.json'))
		input = {
			'plain': sampleInput.get('plain')
		}
		self.assertEqual(getCloudMailAmount(input), 17500)


	def test_getVendorName(self):
		sampleInput = json.load(open('spendTrackerApp/tests/fixtures/cloudmail-sample-body.json'))
		input = {
			'plain': sampleInput.get('plain')
		}
		self.assertEqual(getVendorName(input), 'pacific oculofacial')


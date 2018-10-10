from django.test import TestCase

from ..models import User, Charge



class ChargeModelFunctionalTests(TestCase):
	def setUp(self):
		self.user = User.objects.create(phone_number='123456789')

	def testSaveNewCharge(self):
		Charge.save_new_charge(self.user, 123)
		c = Charge.objects.filter(user_id = self.user, amount=123)
		self.assertEqual(len(c), 1, 'should return one matching row')
		self.assertEqual(c.get().amount, 123, 'should persist the correct amount')

	def testSumByRanges(self):
		Charge.save_new_charge(self.user, 12)
		Charge.save_new_charge(self.user, 34)
		s = Charge.get_sums_by_range()
		self.assertEqual(s.get('amount__sum'), 46)

class UserModelFunctionalTests(TestCase):
	def setUp(self):
		self.phone_number = '6164431505'
		test_user = User(phone_number=self.phone_number)
		test_user.save()

	def test_lookup_user_valid(self):
		"""given a phone number, should return the associated user"""
		found_user = User.lookup_user(self.phone_number).get()
		self.assertEqual(found_user.phone_number, self.phone_number)

	def test_lookup_user_invalid(self):
		empty_result = User.lookup_user('12345')
		self.assertEqual(empty_result, None)

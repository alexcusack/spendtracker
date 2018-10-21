from django.test import TestCase
from ..chat import *
from ..models import User

# 		message_to_reply
# get_reply_string
# create_twilio_reply
class ChatGetReplyTestCases(TestCase):

	def setup(self):
		None

	def test_unmatched_string(self):
		"""Given an unmatched input should return the default output"""
		params = {
			'Body': 'blah',
			'From': '+112345678'
		}
		self.assertEqual(get_reply_string(params), message_to_reply.get('default'))

	def test_given_signup_should_return_with_signup_prompt(self):
		params = {
			'Body': ' siGNUp ',
			'From': '12345678'
		}
		expected = message_to_reply.get('signup').format(phone=params.get('From'))
		self.assertEqual(get_reply_string(params), expected)


class ChatCreateTwilioReply(TestCase):
	def setup(self):
		None

	def test_should_return_xml_formatted_twilio_reply(self):
		reply = create_twilio_reply('hello world')
		self.assertEqual(reply, '<?xml version="1.0" encoding="UTF-8"?><Response><Message>hello world</Message></Response>')


class ChatTestAPISignature(TestCase):
	def setup(self):
		None

	def test_should_handle_random_prompt(self):
		params = {
			'Body': 'geyfghjadhfl', 
			'From': '+12345678'
		}
		resp = self.client.post('/chat/', params)
		self.assertEquals(resp.status_code, 200)
		respBody = resp.content.decode('UTF-8')
		self.assertEquals(respBody, create_twilio_reply(message_to_reply.get('default')))

	def test_should_return_signup_email_when_user_signs_up(self):
		"""If a user messages in 'signup', we should sign them up and respond with the email for them to use"""
		params = {
			'Body': ' siGnUp ', 
			'From': '+12345678'
		}
		resp = self.client.post('/chat/', params)
		self.assertEquals(resp.status_code, 200)
		respBody = resp.content.decode('UTF-8')
		# TODO, it would be better to just assert against the meaningful part of the return string
		self.assertEquals(respBody, create_twilio_reply(get_reply_string(params)))

	def test_should_create_the_user_on_signup(self):
		params = {
			'Body': ' siGnUp ', 
			'From': '+12345678'
		}
		resp = self.client.post('/chat/', params)
		self.assertEquals(resp.status_code, 200)
		user = User.objects.get(phone_number='2345678')
		self.assertEquals(user.phone_number, '2345678')


class UserCreationTest(TestCase):
	def setup(self):
		None

	def test_creates_and_returns_a_user(self):
		user = create_user('+12345678')
		self.assertEqual(user.phone_number, '2345678')

	def test_returns_a_user_if_they_already_exist(self):
		u = User(phone_number='23456789')
		u.save
		user = create_user('+123456789')
		self.assertEqual(user.phone_number, '23456789')








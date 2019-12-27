import json

from django.contrib.auth.models import User
from django.test import TestCase

from message.models import Message


class ComposePageTest(TestCase):

    def test_uses_compose_template(self):
        '''Test that the home page uses the correct compose template.'''
        response = self.client.get('')
        self.assertTemplateUsed(response, 'message/compose.html')

class MessageModelTest(TestCase):

    def test_can_create_message(self):
        '''Test the creation of a Message object.'''
        recipient = User.objects.create(username='recipient')
        sender = User.objects.create(username='sender')
        message = Message.objects.create(recipient=recipient, sender=sender,
                                         message='hello')
        self.assertEqual(message.recipient.username, 'recipient')
        self.assertEqual(message.sender.username, 'sender')
        self.assertEqual(message.message, 'hello')

class ReceivedEndpointTest(TestCase):

    def test_can_get_received_messages(self):
        '''Test that /received endpoint returns the received messages of
        the logged in user.'''
        user1 = User.objects.create(username='user1', password='pass')
        user2 = User.objects.create(username='user2', password='pass')
        Message.objects.create(recipient=user1, sender=user2,
                               message='message1')
        Message.objects.create(recipient=user1, sender=user2,
                               message='message2')
        Message.objects.create(recipient=user1, sender=user2,
                               message='message3')
    
        self.client.force_login(user1)
        response = self.client.get('/received/')
        response_content = json.loads(response.content)
        received_messages = []
        for message in response_content['messages']:
            received_messages.append(message['message'])
        self.assertIn('message1', received_messages)
        self.assertIn('message2', received_messages)
        self.assertIn('message3', received_messages)

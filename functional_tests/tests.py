import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SendMessageTest(unittest.TestCase):

    def setUp(self):
        '''Open two Firefox browsers and log in as both test users in the
        Django admin interface.'''
        self.browser1 = webdriver.Firefox()
        self.browser2 = webdriver.Firefox()

        self.browser1.get('http://localhost:8000/admin/')
        browser1username = self.browser1.find_element_by_id('id_username')
        browser1password = self.browser1.find_element_by_id('id_password')
        browser1username.send_keys('user1')
        browser1password.send_keys('pass')
        browser1password.send_keys(Keys.ENTER)

        self.browser2.get('http://localhost:8000/admin/')
        browser2username = self.browser2.find_element_by_id('id_username')
        browser2password = self.browser2.find_element_by_id('id_password')
        browser2username.send_keys('user2')
        browser2password.send_keys('pass')
        browser2password.send_keys(Keys.ENTER)


    def tearDown(self):
        '''Close Firefox web browser.'''
        self.browser1.quit()
        self.browser2.quit()

    def test_can_send_message(self):
        '''As user1, send a message to user2. Ensure message shows up in
        user2's received messages.'''
        self.browser1.get('http://localhost:8000')
        self.browser2.get('http://localhost:8000')

        recipient_box = self.browser1.find_element_by_id('id_recipient')
        message_box = self.browser1.find_element_by_id('id_message')

        recipient_box.send_keys('user2')
        message_box.send_keys('hello')
        message_box.send_keys(Keys.ENTER)
        
        # Wait 10 seconds before checking if message appeared
        time.sleep(10)

        received_messages = \
            self.browser2.find_element_by_id('received_messages').text
        self.assertIn('hello', received_messages)

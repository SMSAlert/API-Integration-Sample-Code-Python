# -*- coding: utf-8 -*-

import json
import requests


class smsAlertException(Exception):

    def __init__(self, message):
        self.message = message

    def get_message(self):
        return self.message


class smsAlertMsg(object):
    """A simple Python API for the smsAlert

    It includes methods for calling sms api of smsAlert
    """

    def __init__(self, api_key, **kwargs):
        self.auth_key = api_key

        self.sender_id = kwargs.get('sender_id') or 'CVTECH'
        self.route = kwargs.get('route') or 'nondnd'

        self.sms_url = 'http://smsalert.co.in/api/push.json?'


    def send_sms(self, message, mobile):
        res = requests.get(self.sms_url,
                           params={'apikey': self.auth_key,
                                   'mobileno': mobile,
                                   'text': message,
                                   'sender': self.sender_id,
                                   'route': self.route,
                                   'response': 'json'})
        return json.loads(res.content)
    
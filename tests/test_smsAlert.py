#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_smsAlert
----------------------------------

Tests for `smsAlert` module.
"""

import unittest

from smsAlert import smsAlertMsg


class TestsmsAlertMsg(unittest.TestCase):

    def setUp(self):
        api_key = ''  # add your api key for sending SMSs
        app_key = ''  # add your Application Key for testing OTP APIs
        self.client = smsAlertMsg(api_key=api_key, app_key=app_key)

    def tearDown(self):
        pass

    def test_send_sms(self):
        self.client.send_sms('9971XXXXXX','Test SMS', 'CVDEMO', 'demo')

    def test_check_otp_status(self):
        self.client.check_otp_status('9971XXXXXX', 'adbkhDGvad72t8HJDVd396HD')

    def test_send_otp(self):
        self.client.generate_otp('9971XXXXXX')

    def test_verify_otp(self):
        self.client.verify_otp('9971XXXXX', '6264')


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())

===============================
smsAlert Python Sample Code
===============================

A simple python client for smsAlert APIs

* Free software: ISC license

Features
--------

* Send sms to any mobile number using apikey, senderid, route.


Requirements
--------

* apikey : Api Key(This key is unique for every user)

* number : single mobile number (Keep number in international format)

* message : Message Content to send

* senderid : Receiver will see this as sender's ID

* route : If your operator supports multiple routes then give one route name

* senderno : Sender Mobile No

How to use
--------

//import smsAlert.py where you want to send msg

	from .smsAlert import smsAlertMsg

	class smsAlertMsg(unittest.TestCase):
   
    def setUp(self):
		api_key = ''  # add your api key for sending SMSs
		senderid = ''  # add your 6 digit sender's ID
		route = ''  # add your route
	
	self.client = smsAlertMsg(api_key=api_key, sender_id=senderid, route=route)

    def tearDown(self):
        pass

    def test_send_sms(self):
        self.client.send_sms('Test SMS', '9971XXXXXX')
		
	if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())	


Credits
---------

This package was created with Cozy Vision Pvt. Ltd.

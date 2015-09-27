from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC7032c3035db27d10b0baba800d6833a9"
auth_token  = "179430f01ded91585f4d29a4e72673d8"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Showcasing Twilio REST API ",
    to="+918553417378",    # Replace with your phone number
    from_="+14806668530") # Replace with your Twilio number
print message.sid

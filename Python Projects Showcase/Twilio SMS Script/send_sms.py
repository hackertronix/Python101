from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACf52f7b1fad2fd847d2e0be281371b517"
auth_token  = "39b6ea6666e1888afda689eda1ea7b52"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Showcasing Twilio REST API ",
    to="+918792151341",    # Replace with your phone number
    from_="+14348794109") # Replace with your Twilio number
print message.sid

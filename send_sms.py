from twilio.rest import Client

# Authenticate client
client = Client(account_sid, auth_token)

# Send message from twilio phone number to mobile phone number.
message = client.messages.create(
        to = mobile_num, 
        from_= twilio_num,
        body="Hello from Twilio API! Have a nice day")

print(message.sid)

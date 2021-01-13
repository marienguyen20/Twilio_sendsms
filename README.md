## Twilio_sendsms
## Twilio SMS Python Quickstart
Sign up for - or sign in to - Twilio
If you already have a Twilio account go ahead and skip step.
Unless
You can sign up for a free Twilio trial account here: 

When you sign up, you'll be asked to verify your personal phone number. This helps Twilio verify your identity and also allows you to send test messages to your phone from your Twilio account while in trial mode.
Once you verify your number, you'll be asked a series of questions to customize your experience.
Once you finish the onboarding flow, you'll arrive at your project dashboard in the Twilio Console. This is where you'll be able to access your Account SID, authentication token, find a Twilio phone number, and more.

## Send a messeage with Python
Now that we have Python and twilio-python installed, we can send an outbound text message from the Twilio phone number we just purchased with a single API request. Create and open a new file called send_sms.py and type or paste in this code sample.

### Replace the placeholder credential values
Swap the placeholder values for account_sid and auth_token with your personal Twilio credentials. Go to https://www.twilio.com/console and log in. On this page, you’ll find your unique Account SID and Auth Token, which you’ll need any time you send messages through the Twilio Client. 

Open send_sms.py and replace the values for account_sid and auth_token with your unique values.

### Replace the phone number after "from" and "to"
Make sure the phone number using the following format:
[+][country code][phone number including area code]

### Save your changes and run this script from your terminal
python send_sms.py

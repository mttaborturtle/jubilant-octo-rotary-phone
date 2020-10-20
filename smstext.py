from twilio.rest import Client

# Input the body of the text
text_body = input('What would you like to say? :')

# Set the account key and the auth token from your own keys
account_sid = "ACXXXxxXXxxxxXXxxxXXXxxXXXxxXXXXx"
auth_token = "XXxxXXXxxXXxXXXxXXXXXxxxXXXXxxXXX"

client = Client(account_sid, auth_token)

# Add your own phone numbers
client.api.account.messages.create(
    to="+15035552345",
    from_="+16595553456",
    body=text_body)

print('Message has been sent!')

import requests

# Microsoft 365 tenant ID and application credentials
tenant_id = '<YOUR_TENANT_ID>'
client_id = '<YOUR_CLIENT_ID>'
client_secret = '<YOUR_CLIENT_SECRET>'

# Sender and recipient email addresses
sender_email = '<SENDER_EMAIL>'
recipient_email = '<RECIPIENT_EMAIL>'

# Email details
email_subject = '<EMAIL_SUBJECT>'
email_body = '<EMAIL_BODY>'

# Get access token
def get_access_token():
    url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': 'https://graph.microsoft.com/.default'
    }
    response = requests.post(url, data=data)
    access_token = response.json()['access_token']
    return access_token

# Send email
def send_email(access_token):
    url = 'https://graph.microsoft.com/v1.0/users/{sender_email}/sendMail'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    data = {
        'message': {
            'subject': email_subject,
            'body': {
                'contentType': 'Text',
                'content': email_body
            },
            'toRecipients': [
                {
                    'emailAddress': {
                        'address': recipient_email
                    }
                }
            ]
        }
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 202:
        print('Email sent successfully!')
    else:
        print('Failed to send email.')

# Main function
def main():
    access_token = get_access_token()
    send_email(access_token)

# Run the program
main()

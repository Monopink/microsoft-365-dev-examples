import requests

# Microsoft 365 tenant ID and application credentials
tenant_id = '<YOUR_TENANT_ID>'
client_id = '<YOUR_CLIENT_ID>'
client_secret = '<YOUR_CLIENT_SECRET>'

# Mailbox details
mailbox_email = '<MAILBOX_EMAIL>'  # Example: 'user@example.com'

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

# Get emails from mailbox
def get_emails(access_token):
    url = f'https://graph.microsoft.com/v1.0/users/{mailbox_email}/messages'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        emails = response.json()['value']
        for email in emails:
            print('Subject:', email['subject'])
            print('Sender:', email['sender']['emailAddress']['address'])
            print('Received:', email['receivedDateTime'])
            print('Body:', email['body']['content'])
            print('---')
    else:
        print('Failed to retrieve emails.')

# Main function
def main():
    access_token = get_access_token()
    get_emails(access_token)

# Run the program
main()

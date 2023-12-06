import requests

# Define the parameters for Microsoft Graph API
tenant_id = 'YOUR_TENANT_ID'
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
scope = 'https://graph.microsoft.com/.default'

# Get the access token
def get_access_token():
    url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'
    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
        'scope': scope
    }
    response = requests.post(url, data=data)
    access_token = response.json()['access_token']
    return access_token

# Create a new Word document
def create_word_document(access_token, filename):
    url = 'https://graph.microsoft.com/v1.0/me/drive/root/children'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    data = {
        'name': filename,
        'file': {}
    }
    response = requests.post(url, headers=headers, json=data)
    document_id = response.json()['id']
    return document_id

# Add content to the Word document
def add_content_to_document(access_token, document_id, content):
    url = f'https://graph.microsoft.com/v1.0/me/drive/items/{document_id}/content'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'text/plain'
    }
    response = requests.put(url, headers=headers, data=content)
    if response.status_code == 200:
        print('Content has been successfully added to the document!')
    else:
        print('Unable to add content to the document.')

# Main function
def main():
    access_token = get_access_token()
    document_id = create_word_document(access_token, 'MyDocument.docx')
    content = 'This is a sample document for Microsoft 365 programming.'
    add_content_to_document(access_token, document_id, content)

# Run the main function
main()

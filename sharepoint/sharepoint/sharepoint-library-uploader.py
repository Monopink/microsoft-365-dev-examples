import requests
import json

# Microsoft 365 tenant ID and application credentials
tenant_id = '<YOUR_TENANT_ID>'
client_id = '<YOUR_CLIENT_ID>'
client_secret = '<YOUR_CLIENT_SECRET>'

# SharePoint details
site_url = '<SITE_URL>'  # Example: 'https://yourtenant.sharepoint.com/sites/your-site'
library_name = '<LIBRARY_NAME>'  # Example: 'Documents'
file_name = '<FILE_NAME>'  # Example: 'example.docx'

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

# Get SharePoint library ID
def get_library_id(access_token):
    url = f'{site_url}/_api/web/lists'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        libraries = response.json()['value']
        for library in libraries:
            if library['BaseTemplate'] == 101 and library['Title'] == library_name:
                return library['Id']
        print('Library not found.')
        return None
    else:
        print('Failed to retrieve libraries.')
        return None

# Upload file to SharePoint library
def upload_file(access_token, library_id):
    url = f'{site_url}/_api/web/lists(guid\'{library_id}\')/RootFolder/Files/add(url=\'{file_name}\',overwrite=true)'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    with open(file_name, 'rb') as file:
        data = file.read()
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            print('File uploaded successfully!')
        else:
            print('Failed to upload file.')

# Main function
def main():
    access_token = get_access_token()
    library_id = get_library_id(access_token)
    if library_id:
        upload_file(access_token, library_id)

# Run the program
main()

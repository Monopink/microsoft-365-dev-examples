import requests

# Microsoft 365 tenant ID and application credentials
tenant_id = '<YOUR_TENANT_ID>'
client_id = '<YOUR_CLIENT_ID>'
client_secret = '<YOUR_CLIENT_SECRET>'

# SharePoint details
site_url = '<SITE_URL>'  # Example: 'https://yourtenant.sharepoint.com/sites/your-site'
folder_name = '<FOLDER_NAME>'  # Example: 'Documents'
file_path = '<FILE_PATH>'  # Example: 'C:/path/to/file.txt'

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

# Upload file to SharePoint
def upload_file(access_token):
    url = f'{site_url}/_api/web/GetFolderByServerRelativeUrl(\'/{folder_name}\')/Files/add(url=\'{file_path}\',overwrite=true)'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    with open(file_path, 'rb') as file:
        data = file.read()
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            print('File uploaded successfully!')
        else:
            print('Failed to upload file.')

# Main function
def main():
    access_token = get_access_token()
    upload_file(access_token)

# Run the program
main()

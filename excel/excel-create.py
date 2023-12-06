import requests

# Microsoft 365 tenant ID and application credentials
tenant_id = '<YOUR_TENANT_ID>'
client_id = '<YOUR_CLIENT_ID>'
client_secret = '<YOUR_CLIENT_SECRET>'

# New Excel file details
file_name = '<FILE_NAME>'  # Example: 'NewFile.xlsx'
sheet_name = '<SHEET_NAME>'  # Example: 'Sheet1'
cell_value = '<CELL_VALUE>'  # Example: 'Hello, World!'

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

# Create new Excel file
def create_excel_file(access_token):
    url = 'https://graph.microsoft.com/v1.0/me/drive/root/children'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    data = {
        'name': file_name,
        'file': {},
        '@microsoft.graph.conflictBehavior': 'rename'
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print('Excel file created successfully!')
        response_json = response.json()
        drive_item_id = response_json['id']
        update_excel_file(access_token, drive_item_id)
    else:
        print('Failed to create Excel file.')

# Update Excel file with data
def update_excel_file(access_token, drive_item_id):
    url = f'https://graph.microsoft.com/v1.0/me/drive/items/{drive_item_id}/workbook/worksheets/{sheet_name}/range(address=\'A1\')'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    data = {
        'values': [[cell_value]]
    }
    response = requests.patch(url, headers=headers, json=data)
    if response.status_code == 200:
        print('Excel file updated successfully!')
    else:
        print('Failed to update Excel file.')

# Main function
def main():
    access_token = get_access_token()
    create_excel_file(access_token)

# Run the program
main()

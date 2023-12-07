import requests

# Microsoft 365 tenant ID and application credentials
tenant_id = '<YOUR_TENANT_ID>'
client_id = '<YOUR_CLIENT_ID>'
client_secret = '<YOUR_CLIENT_SECRET>'

# Excel file details
file_name = '<FILE_NAME>'  # Example: 'SampleFile.xlsx'
sheet_name = '<SHEET_NAME>'  # Example: 'Sheet1'
cell_address = '<CELL_ADDRESS>'  # Example: 'A1'
new_cell_value = '<NEW_CELL_VALUE>'  # Example: 'New Value'

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

# Update Excel file with new value
def update_excel_file(access_token):
    url = f'https://graph.microsoft.com/v1.0/me/drive/root:/{file_name}:/workbook/worksheets/{sheet_name}/range(address=\'{cell_address}\')'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    data = {
        'values': [[new_cell_value]]
    }
    response = requests.patch(url, headers=headers, json=data)
    if response.status_code == 200:
        print('Excel file updated successfully!')
    else:
        print('Failed to update Excel file.')

# Main function
def main():
    access_token = get_access_token()
    update_excel_file(access_token)

# Run the program
main()

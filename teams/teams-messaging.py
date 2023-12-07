import requests

# Microsoft 365 tenant ID and application credentials
tenant_id = '<YOUR_TENANT_ID>'
client_id = '<YOUR_CLIENT_ID>'
client_secret = '<YOUR_CLIENT_SECRET>'

# Teams details
team_name = '<TEAM_NAME>'  # Example: 'My Team'
channel_name = '<CHANNEL_NAME>'  # Example: 'General'
message_content = '<MESSAGE_CONTENT>'  # Example: 'Hello, everyone!'

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

# Get team ID
def get_team_id(access_token):
    url = 'https://graph.microsoft.com/v1.0/me/joinedTeams'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        teams = response.json()['value']
        for team in teams:
            if team['displayName'] == team_name:
                return team['id']
        print('Team not found.')
        return None
    else:
        print('Failed to retrieve teams.')
        return None

# Get channel ID
def get_channel_id(access_token, team_id):
    url = f'https://graph.microsoft.com/v1.0/teams/{team_id}/channels'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        channels = response.json()['value']
        for channel in channels:
            if channel['displayName'] == channel_name:
                return channel['id']
        print('Channel not found.')
        return None
    else:
        print('Failed to retrieve channels.')
        return None

# Send message to channel
def send_message(access_token, team_id, channel_id):
    url = f'https://graph.microsoft.com/v1.0/teams/{team_id}/channels/{channel_id}/messages'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    data = {
        'body': {
            'content': message_content
        }
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print('Message sent successfully!')
    else:
        print('Failed to send message.')

# Main function
def main():
    access_token = get_access_token()
    team_id = get_team_id(access_token)
    if team_id:
        channel_id = get_channel_id(access_token, team_id)
        if channel_id:
            send_message(access_token, team_id, channel_id)

# Run the program
main()

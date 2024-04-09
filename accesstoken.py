import requests
#api_key = "YOUR KEY HERE!"
# Set your client ID and client secret obtained from the Spotify Developer Dashboard
client_id = '3c433e73a0284af0bcbec2e9980440f5'
client_secret = '650b672f80674cadbca01f7bed77f375'

# Set the token endpoint
token_url = 'https://accounts.spotify.com/api/token'

# Step 2: Exchange the authorization code for an access token
token_params = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret
}
token_response = requests.post(token_url, data=token_params)

# Extract the access token from the token response
access_token = token_response.json()['access_token']
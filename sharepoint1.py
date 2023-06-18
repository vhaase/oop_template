import requests

# Set up the necessary parameters
client_id = '98c7659b-526c-44ea-b3e8-b7cac058ca25'
client_secret = '4SSsPn0sNorHz5uiB0rCaSTGxhd1rLyWFlM2QUcystQ='
tenant_id = '18a29fd9-ba54-48a9-9f78-ad7ad16d433b'
resource = 'https://haasebusiness-my.sharepoint.com'

# Get an Access token using client Credentials
auth_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
auth_data = {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
    'scope': f'{resource}/.default'
}
response = requests.post(auth_url, data=auth_data)
access_token = response.json().get('access_token')

# Make a request to get the list of filelist in the folder
folder_id = '/personal/volker_haasebusiness_de/Documents/'
files_url = f'{resource}/v1.0/drives/{folder_id}/Betrieb/'
headers = {
    'Authorization': f'Bearer {access_token}',
    'Accept': 'application/json'
}
response = requests.get(files_url, headers=headers)
files = response.json().get('value')

# Print the names of the filelist
for file in files:
    print(file['name'])

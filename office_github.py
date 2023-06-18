# pip install Office365-REST-Python-Client
# pip install git+https://github.com/vgrem/Office365-REST-Python-Client.git

# courtesy: https://stackoverflow.com/questions/59979467/accessing-microsoft-sharepoint-files-and-data-using-python

# Importing required libraries

from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File

# Constrtucting SharePoint URL and Credentials

sharepoint_base_url = 'https://mycompany.sharepoint.com/teams/volker_haasebusiness_de/'
sharepoint_user = '75d8cc58-bce3-4140-85a9-7ee8ba0281ce'
sharepoint_password = 'e0fGDx1I/+HDf4JnJUDXm18ra9MHeQHVNU9mBFbX5bE='
folder_in_sharepoint = '/teams/volker_haasebusiness_de/Shared%20Documents/haasebusiness/'

# Constructing Details For Authenticating SharePoint

auth = AuthenticationContext(sharepoint_base_url)

auth.acquire_token_for_user(sharepoint_user, sharepoint_password)
ctx = ClientContext(sharepoint_base_url, auth)
web = ctx.web
ctx.load(web)
ctx.execute_query()
print('Connected to SharePoint: ', web.properties['Title'])


# Constructing Function for getting fileentry details in SharePoint Folder

def folder_details(ctx, folder_in_sharepoint):
    folder = ctx.web.get_folder_by_server_relative_url(folder_in_sharepoint)
    fold_names = []
    sub_folders = folder.filelist
    ctx.load(sub_folders)
    ctx.execute_query()
    for s_folder in sub_folders:
        fold_names.append(s_folder.properties["Name"])


    return fold_names

# Getting folder details

file_list = folder_details(ctx, folder_in_sharepoint)

# Printing list of filelist from sharepoint folder
print(file_list)

# Reading File from SharePoint Folder
sharepoint_file = '/teams/SustainabilityDataAccelerator/Shared%20Documents/General/Agro/2018_indirects_sustainable_sourcing_template.xlsx'
file_response = File.open_binary(ctx, sharepoint_file)

# Saving fileentry to local
with open("sharepointfile.csv", 'wb') as output_file:
    output_file.write(file_response.content)

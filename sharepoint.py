# handling of files on SharePoint

import office365.runtime.auth.authentication_context
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.system_object_type import FileSystemObjectType


class SharePoint:
    def __init__(self):
        self.alleFolder = None
        self.folderlist = None
        self.meinfolder = None
        self.web = None
        self.file = None
        self.folder_relative_url = None
        self.files = None
        self.folder = None
        self.ctx = None
        self.ctx_auth = None
        self.older_relative_url = None
        self.client_secret = None
        self.client_id = None
        self.site_url = None

    def access(self):
        # die zugangsdaten, vorläufig hardcoded

        self.site_url = "https://haasebusiness-my.sharepoint.com/personal/volker_haasebusiness_de"
        # self.client_id = '4faad7c2-9eee-4c24-ac71-24b04ad42151'
        self.client_id = '98c7659b-526c-44ea-b3e8-b7cac058ca25'
        # self.client_secret = 'pzl8vrWrgqi3vtbJXtWUCHcxhTBaUuOstA5RpCHYBwQ='
        self.client_secret = '4SSsPn0sNorHz5uiB0rCaSTGxhd1rLyWFlM2QUcystQ='
        self.folder_relative_url = '/personal/volker_haasebusiness_de/'

        # Authenticate using client credentials

        try:
            self.ctx_auth = AuthenticationContext(self.site_url)
            self.ctx_auth.acquire_token_for_app(self.client_id, self.client_secret)
            self.ctx = ClientContext(self.site_url, self.ctx_auth)

            self.web = self.ctx.web
            self.ctx.load(self.web)
            self.ctx.execute_query()
            print('Connected to SharePoint: ', self.web.properties['Title'])

            # Get the folder list
            self.folderlist = self.ctx.web.lists.get_by_title("Dokumente")
            self.alleFolder = self.folderlist.items.select(["FileSystemObjectType"]).expand(["File", "Folder"]).get().execute_query()
            # Print the names of the folders
            for item in self.alleFolder:  # type: ListItem
                if item.file_system_object_type == FileSystemObjectType.Folder:
                    print(item.folder.serverRelativeUrl)
                else:
                    print(item.file.serverRelativeUrl)
            print("\n\nliste fertig")

            # Get the folder
            self.folder = self.ctx.web.get_folder_by_server_relative_url(self.folder_relative_url)
            self.ctx.load(self.folder)
            self.ctx.execute_query()

            # Get the files in the folder
            self.files = self.folder.files
            self.ctx.load(self.files)
            self.ctx.execute_query()

            # Print the names of the files
            for self.file in self.files:
                print(self.file.properties["Name"])
        except Exception as e:
            print("oops: ", e)

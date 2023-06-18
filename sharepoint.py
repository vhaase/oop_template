# handling of filelist on SharePoint
from credentials import Credentials
from access import Access

# from office365.runtime.auth.authentication_context import AuthenticationContext
# from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.system_object_type import FileSystemObjectType


class SharePoint:
    def __init__(self):
        self.fileentry = None
        self.filelist = None
        self.folder = None
        self.alleFolder = None
        self.folderlist = None
        self.ctx_auth = None
        self.web = None
        self.ctx = None
        self.cred = Credentials()

    def accessFolders(self):
        # Authenticate using client Credentials
        self.ctx = Access.contxt(self)

        try:
            # Get the folder list
            self.folderlist = self.ctx.web.lists.get_by_title("Dokumente")
            self.alleFolder = self.folderlist.items.select(["FileSystemObjectType"]).expand(
                ["File", "Folder"]).get().execute_query()
            # Print the names of the folders
            for item in self.alleFolder:
                if item.file_system_object_type == FileSystemObjectType.Folder:
                    print(item.folder.serverRelativeUrl)
                else:
                    print(item.fileentry.serverRelativeUrl)
            print("\n\nliste fertig")

            # Get the folder
            self.folder = self.ctx.web.get_folder_by_server_relative_url(self.cred.folder_relative_url)
            self.ctx.load(self.folder)
            self.ctx.execute_query()

            # Get the filelist in the folder
            self.filelist = self.folder.filelist
            self.ctx.load(self.filelist)
            self.ctx.execute_query()

            # Print the names of the filelist
            for self.fileentry in self.filelist:
                print(self.fileentry.properties["Name"])
        except Exception as e:
            print("oops: ", e)
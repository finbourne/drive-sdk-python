import os
from lusid_drive import api as ld
from lusid_drive import ApiClientBuilder


def name_to_id(item_list, target_item):
    item_id = [obj.id for obj in item_list.values if obj.name == target_item]

    if len(item_id) != 1:
        # TODO: raise an exception due to no matching item name, or multiple matches
        pass

    else:
        return item_id[0]


class LusidDriveTestFunctions:
    def __init__(self):
        self.api_client = ApiClientBuilder().build("secrets.json")
        self.folders_api = ld.FoldersApi(self.api_client)
        self.files_api = ld.FilesApi(self.api_client)

    def create_file(self, local_file_path, target_drive_folder):
        response = self.files_api.create_file(
            x_lusid_drive_filename=local_file_path.split("/")[-1],
            x_lusid_drive_path=f"/{target_drive_folder}",
            content_length=os.stat(local_file_path).st_size,
            body=local_file_path
        )

        return response

    def get_folder_id(self, folder_name):
        response = self.folders_api.get_root_folder()
        folder_id = name_to_id(response, folder_name)

        return folder_id

    def get_file_id(self, file_name, folder_id):
        response = self.folders_api.get_folder_contents(folder_id)
        file_id = name_to_id(response, file_name)

        return file_id

    def download_file(self, file_name, folder_name):
        folder_id = self.get_folder_id(folder_name)
        file_id = self.get_file_id(file_name, folder_id)
        response = self.files_api.download_file(file_id)

        return response

    def delete_file(self, file_name, folder_name):
        folder_id = self.get_folder_id(folder_name)
        file_id = self.get_file_id(file_name, folder_id)
        response = self.files_api.delete_file(file_id)

        return response




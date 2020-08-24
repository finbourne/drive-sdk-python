import unittest
import json
import lusid_drive
import logging
from lusid_drive import api as ld
from lusid_drive import models as models
from lusid_drive import ApiClientBuilder
from tests.test_functions import LusidDriveTestFunctions


class LusidDriveTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:

        cls.logger = logging.getLogger()
        cls.logger.setLevel(logging.INFO)

        cls.api_client = ApiClientBuilder().build("secrets.json")
        cls.folder_api = ld.FoldersApi(cls.api_client)
        cls.files_api = ld.FilesApi(cls.api_client)

        cls.folder_name = "sdk-test-folder2"
        cls.file_name = "test_file.txt"
        cls.local_file_path = "data/test_file.txt"

        cls.test_functions = LusidDriveTestFunctions()

        try:
            cls.folder_api.create_folder(models.CreateFolder(path="/", name=cls.folder_name))

        except lusid_drive.exceptions.ApiException as e:
            if json.loads(e.body)["code"] == 664:
                cls.logger.info(json.loads(e.body)["title"] + ":" + f"{cls.folder_name}")

    def test_get_folder(self):

        get_folder = self.folder_api.get_root_folder()

        list_root_contents = ([folder.name for folder in get_folder.values])

        self.assertIn(self.folder_name, list_root_contents)

    def test_create_file(self):

        try:
            response = self.test_functions.create_file(self.local_file_path, self.folder_name)
            self.assertEqual(self.file_name, response.name)

        except:  # if file already exists
            self.test_functions.delete_file(self.file_name, self.folder_name)
            response = self.test_functions.create_file(self.local_file_path, self.folder_name)
            self.assertEqual(self.file_name, response.name)

    def test_download_file(self):

        try:
            response = self.test_functions.download_file(self.file_name, self.folder_name)
            self.assertIn(self.file_name, response)

        except:  # if 400 exception for file not existing
            temp_response = self.test_functions.create_file(self.local_file_path, self.folder_name)
            response = self.files_api.download_file(temp_response.id)
            self.assertIn(self.file_name, response)

    def test_delete_file(self):

        try:
            response = self.test_functions.delete_file(self.file_name, self.folder_name)
            self.assertEqual(None, response)

        except:  # if 400 exception for file not existing
            temp_response = self.test_functions.create_file(self.local_file_path, self.folder_name)
            response = self.files_api.delete_file(temp_response.id)
            self.assertEqual(None, response)


if __name__ == '__main__':
    unittest.main()

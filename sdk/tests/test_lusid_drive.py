import unittest
import json
import lusid_drive
import logging
from lusid_drive import api as ld
from lusid_drive import models as models
from lusid_drive import ApiClientBuilder

class LusidDriveTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:

        cls.logger = logging.getLogger()
        cls.logger.setLevel(logging.INFO)

        cls.api_client = ApiClientBuilder().build("secrets.json")
        cls.folder_api = ld.FoldersApi(cls.api_client)
        cls.files_api = ld.FilesApi(cls.api_client)

        cls.testing_folder = "sdk-test-folder2"

        try:
            cls.folder_api.create_folder(models.CreateFolder(path="/", name=cls.testing_folder))

        except lusid_drive.exceptions.ApiException as e:
            if json.loads(e.body)["code"] == 664:
                cls.logger.info(json.loads(e.body)["title"] + ":" + f"{cls.testing_folder}")

    def test_get_folder(self):

        get_folder = self.folder_api.get_root_folder()

        list_root_contents = ([folder.name for folder in get_folder.values])

        self.assertIn(self.testing_folder, list_root_contents)


if __name__ == '__main__':
    unittest.main()

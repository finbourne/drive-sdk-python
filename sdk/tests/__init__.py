import unittest

import lusid_drive
from lusid_drive.utilities import ApiConfigurationLoader
from lusid_drive.utilities import ApiClientFactory


class FinbourneAccessTests(unittest.TestCase):

    def test_roles(self):

        config = ApiConfigurationLoader.load("secrets.json")
        api_factory = ApiClientFactory(token=config.api_token, api_url=config.api_url)
        policies_api = api_factory.build(lusid_drive.api.PoliciesApi)

        policies = policies_api.get_own_policies()

        self.assertGreater(len(policies), 0)


if __name__ == '__main__':
    unittest.main()
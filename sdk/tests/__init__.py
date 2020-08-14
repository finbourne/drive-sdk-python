import unittest
from lusid_drive import api as sa

from lusid_drive import ApiClientBuilder


class FinbourneAccessTests(unittest.TestCase):

    def test_roles(self):
        api_client = ApiClientBuilder().build("secrets.json")
        policies_api = sa.PoliciesApi(api_client)

        policies = policies_api.get_own_policies()

        self.assertGreater(len(policies), 0)


if __name__ == '__main__':
    unittest.main()
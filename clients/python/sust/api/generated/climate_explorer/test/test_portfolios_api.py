"""
    Sust Global Climate Explorer API

     This API provides programmatic access to physical risk exposure data. For more guidance on using this API, please visit the Sust Global Dev Center: https://developers.sustglobal.com.   # noqa: E501

    The version of the OpenAPI document: beta
    Generated by: https://openapi-generator.tech
"""


import unittest

import sust.api.generated.climate_explorer
from sust.api.generated.climate_explorer.api.portfolios_api import PortfoliosApi  # noqa: E501


class TestPortfoliosApi(unittest.TestCase):
    """PortfoliosApi unit test stubs"""

    def setUp(self):
        self.api = PortfoliosApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_portfolios_assets_export_list(self):
        """Test case for portfolios_assets_export_list

        Export Portfolio Assets  # noqa: E501
        """
        pass

    def test_portfolios_assets_import_create(self):
        """Test case for portfolios_assets_import_create

        Import Portfolio Assets  # noqa: E501
        """
        pass

    def test_portfolios_assets_list(self):
        """Test case for portfolios_assets_list

        List Portfolio Assets  # noqa: E501
        """
        pass

    def test_portfolios_create(self):
        """Test case for portfolios_create

        Create Portfolio  # noqa: E501
        """
        pass

    def test_portfolios_datasets_physical_export_list(self):
        """Test case for portfolios_datasets_physical_export_list

        Export Physical Risk Exposure Dataset  # noqa: E501
        """
        pass

    def test_portfolios_datasets_physical_items_list(self):
        """Test case for portfolios_datasets_physical_items_list

        Get Physical Risk Exposure Data  # noqa: E501
        """
        pass

    def test_portfolios_datasets_physical_list(self):
        """Test case for portfolios_datasets_physical_list

        Get Physical Risk Exposure Metadata  # noqa: E501
        """
        pass

    def test_portfolios_datasets_physical_summary_list(self):
        """Test case for portfolios_datasets_physical_summary_list

        Get Physical Risk Exposure Summary  # noqa: E501
        """
        pass

    def test_portfolios_delete(self):
        """Test case for portfolios_delete

        Delete Portfolio  # noqa: E501
        """
        pass

    def test_portfolios_list(self):
        """Test case for portfolios_list

        List Portfolios  # noqa: E501
        """
        pass

    def test_portfolios_read(self):
        """Test case for portfolios_read

        Get Portfolio  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
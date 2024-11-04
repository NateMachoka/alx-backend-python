#!/usr/bin/env python3
"""Tests the GitHubOrgClient class"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')  # Patch the get_json method
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""

        # Define the expected return value for get_json
        mock_get_json.return_value = {
            "repos_url": "https://api.github.com/orgs/{org}/repos"}

        # Create an instance of GithubOrgClient with the org_name
        client = GithubOrgClient(org_name)

        # Call the org method
        result = client.org()

        # Assertions
        mock_get_json.assert_called_once_with(
            client.ORG_URL.format(org=org_name))
        self.assertEqual(result, mock_get_json.return_value)


if __name__ == "__main__":
    unittest.main()

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

    @patch('client.GithubOrgClient.org')
    def test_public_repos_url(self, mock_org):
        """Test that _public_repos_url returns the expected URL"""

        # Define a known payload to be returned by the mocked org method
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/test-org/repos"
        }

        # Create an instance of GithubOrgClient
        client = GithubOrgClient("test-org")

        # Access the _public_repos_url property
        result = client._public_repos_url

        # Assertions
        self.assertEqual(result, "https://api.github.com/orgs/test-org/repos")

     @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that GithubOrgClient.public_repos returns the expected list of repositories"""

        # Define the mock payload for get_json
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]

        # Use patch as a context manager to mock _public_repos_url
        with patch('client.GithubOrgClient._public_repos_url', new_callable=property) as mock_repos_url:
            # Set the return value for the _public_repos_url property
            mock_repos_url.return_value = "https://api.github.com/orgs/test-org/repos"

            # Create an instance of GithubOrgClient
            client = GithubOrgClient("test-org")

            # Call the public_repos method
            result = client.public_repos()

            # Expected list of repo names
            expected_repos = ["repo1", "repo2", "repo3"]

            # Assertions
            self.assertEqual(result, expected_repos)
            mock_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/test-org/repos")



if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
"""Tests the GitHubOrgClient class"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
import fixtures


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
        """Test that GithubOrgClient.public_repos
            returns the expected list of repositories
        """

        # Define the mock payload for get_json
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"}
        ]

        # Use patch as a context manager to mock _public_repos_url
        with patch(
                'client.GithubOrgClient._public_repos_url',
                new_callable=property
        ) as mock_repos_url:
            # Set the return value for the _public_repos_url property
            mock_repos_url.return_value =
            "https://api.github.com/orgs/test-org/repos"

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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False),  # Case where repo has no license key
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that GithubOrgClient.has_license
           returns the correct value based on the license
        """

        # Create an instance of GithubOrgClient
        client = GithubOrgClient("test-org")

        # Call has_license and check the result
        result = client.has_license(repo, license_key)

        # Assertion
        self.assertEqual(result, expected)


@parameterized_class([
    {
        "org_payload": fixtures.org_payload,
        "repos_payload": fixtures.repos_payload,
        "expected_repos": fixtures.expected_repos,
        "apache2_repos": fixtures.apache2_repos
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient.public_repos"""

    @classmethod
    def setUpClass(cls):
        """Set up class method to start patching requests.get"""

        # Start patching 'requests.get'
        cls.get_patcher = patch('requests.get')

        # Start the patcher, configure side_effect to return different fixtures
        cls.mock_get = cls.get_patcher.start()

        # Define side_effect for requests.get to return fixture based on URL
        def get_json(url):
            if url == GithubOrgClient.ORG_URL.format(org="google"):
                return Mock(json=lambda: cls.org_payload)
            elif url == cls.org_payload["repos_url"]:
                return Mock(json=lambda: cls.repos_payload)
            return Mock(json=lambda: None)

        cls.mock_get.side_effect = get_json

    @classmethod
    def tearDownClass(cls):
        """Tear down class method to stop patching requests.get"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos method to check expected repository names"""

        # Create an instance of GithubOrgClient with a known organization
        client = GithubOrgClient("google")

        # Call the public_repos method and verify it returns expected_repos
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos method with license filtering"""

        # Create an instance of GithubOrgClient with a known organization
        client = GithubOrgClient("google")

        # Call the public_repos method with 'apache-2.0' license
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)


if __name__ == "__main__":
    unittest.main()

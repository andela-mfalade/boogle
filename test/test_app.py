"""Test Application Instance Properties."""
import unittest
from flask import Flask


from boogle import create_app


class AppTest(unittest.TestCase):
    def setUp(self):
        """Basic App setup.

        Create instance of client to handle requests.
        """
        self.app = create_app('test')
        self.client = self.app.test_client()


    def test_main_route_works_as_expected(self):
        """Test that index route works as expected."""
        vr = self.client.get('/')
        self.assertEqual(vr.status_code, 200)

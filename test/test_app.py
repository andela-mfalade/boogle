"""Test Application Instance Properties."""
import unittest
from flask import Flask


from boogle import create_app


class AppTest(unittest.TestCase):
    def setUp(self):
        """Basic App setup.

        Create instance of client to handle requests.
        """
        self.client = create_app('test')


    def test_returns_flask_app_instance_on_init(self):
        self.assertEqual(self.client, Flask(__name__))

import unittest

import app


class ApiTest(unittest.TestCase):
    def setUp(self):
        self.app = app.app
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    def test_hello(self):
        res = self.client.get("/")

        self.assertEqual(res.data.decode(), "Hello, World!")

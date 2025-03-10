import unittest
from app import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_health_check(self):
        response = self.app.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"status": "ok"})

    def test_get_items(self):
        response = self.app.get("/items")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()

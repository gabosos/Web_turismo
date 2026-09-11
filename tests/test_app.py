import unittest

from app import app


class TravelApiTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Descubre el mundo", response.data)

    def test_destinations_api(self):
        response = self.client.get("/api/destinations")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["count"], 3)

    def test_unknown_destination(self):
        response = self.client.get("/api/destinations/no-existe")
        self.assertEqual(response.status_code, 404)

    def test_contact_api(self):
        response = self.client.post("/api/contact", json={"name": "Ana", "email": "ana@example.com", "message": "Hola"})
        self.assertEqual(response.status_code, 201)

    def test_contact_requires_fields(self):
        response = self.client.post("/api/contact", json={"name": "Ana"})
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()

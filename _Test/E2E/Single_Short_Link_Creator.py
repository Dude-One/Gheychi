import unittest
import requests
import json

class TestCreateAndRedirectFlow(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.ServerConfig = {
            "ServerDoimain": "127.0.0.1",
            "ServerPort": "8000"

        }
        self.addr = self.ServerConfig['ServerDoimain']
        self.port = self.ServerConfig['ServerPort']
        self.URL = 'https://www.iranjib.ir/'

    def test_1_Creating_NewShortLink(self):
        url = f"http://{self.addr}:{int(self.port)}/api/shorten"
        payload = {
            "long_url": self.URL
        }
        response = requests.post(url, json=payload)
        self.assertIn(response.status_code, [200, 201])
        self.assertIn("short_url", response.json())
        self.__class__.Shortesh = response.json()["short_url"]
        print(self.Shortesh )


    def test_2_check_Redirection_on_it(self):
        response = requests.get(self.__class__.Shortesh,allow_redirects=False)
        self.assertIn(response.status_code, [301,302,307])
        print("Redirecting to:", response.headers.get("location"))


    @classmethod
    def tearDownClass(self):
        print('Noting')

if __name__ == "__main__":
    unittest.main()
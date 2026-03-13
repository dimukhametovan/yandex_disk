import requests
from config.config import BASE_URL, YANDEX_DISK_TOKEN


class APIClient:
    def __init__(self):
        self.session = requests.Session()

        self.session.headers = {
            "Authorization": f"OAuth {YANDEX_DISK_TOKEN}",
            "Content-Type": "application/json",
        }

    def request(self, method, endpoint, **kwargs):
        response = self.session.request(
            method=method,
            url=f"{BASE_URL}{endpoint}",
            **kwargs
        )
        return response
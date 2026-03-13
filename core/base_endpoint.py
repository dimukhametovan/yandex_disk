from core.api_client import APIClient
from core.response import Response


class BaseEndpoint:

    def __init__(self):
        self.client = APIClient()

    def request(self, method, endpoint, **kwargs):
        response = self.client.request(method, endpoint, **kwargs)
        return Response(response)
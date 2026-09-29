import requests

from config.settings import settings
from core.logging.logger import Logger
from core.exceptions.api_exception import ApiException


class BaseClient:

    def __init__(self):

        self.base_url = settings.base_url
        self.timeout = settings.timeout

        self.logger = Logger.get_logger(self.__class__.__name__)

        self.session = requests.Session()

        self.session.headers.update({
            "Content-Type": "application/json"
        })

    def _request(self, method: str, endpoint: str, **kwargs):

        url = f"{self.base_url}{endpoint}"

        self.logger.info(f"{method} {url}")

        try:
            response = self.session.request(
                method=method,
                url=url,
                timeout=self.timeout,
                **kwargs
            )

        except requests.RequestException as e:
            self.logger.error(f"Request failed: {str(e)}")
            raise ApiException(f"Request error: {str(e)}")

        self.logger.info(
            f"Response: {response.status_code}"
        )

        return response

    # HTTP Methods

    def get(self, endpoint: str, **kwargs):
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs):
        return self._request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs):
        return self._request("PUT", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs):
        return self._request("DELETE", endpoint, **kwargs)

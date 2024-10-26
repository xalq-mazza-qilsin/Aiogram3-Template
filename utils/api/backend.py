from .base import BaseAPIClient
from data.config import BACKEND_HOST


class BotAPIClient(BaseAPIClient):
	def __init__(self):
		super().__init__()
		self.api_base_url = f"{BACKEND_HOST.rstrip('/')}/api/v1"
		self.bot_base_url = self.api_base_url + "/bot"


bot_api_client = BotAPIClient()

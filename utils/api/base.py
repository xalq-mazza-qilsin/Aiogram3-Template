import aiohttp


class BaseAPIClient:
	def __init__(self):
		self.session = aiohttp.ClientSession()

	async def _send_request(
			self,
			method,
			url,
			json=None,
			headers=None,
	):

		response = await self.session.request(
			method=method, url=url, json=json, headers=headers
		)
		return await response.json()

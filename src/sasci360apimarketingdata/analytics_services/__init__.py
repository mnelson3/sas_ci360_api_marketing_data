#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apimarketingdata.base import Base


class AnalyticsServices(Base):
	"""
	Analytics Services Module
	Contains the operations for the analytic services.
		1. get_analytics_services(self) -> requests.Response
		2. get_transfer_items(self, **kwargs) -> requests.Response
		3. get_transfer_item(self, transfer_id: str) -> requests.Response
		4. create_transfer_location(self, payload: dict) -> requests.Response
	"""

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_analytics_services(self) -> requests.Response:
		"""
		Access analytic services
		:return: Get the links to analytic services or items.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/analytic"
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_transfer_items(self, **kwargs) -> requests.Response:
		"""
		Return a collection of transfer items
		:keyword sort_by: str, optional - Specify the sort field and order for transfer result collection
		:keyword start: int, optional - The index of the first transfer item to return. The default value is 0
		:keyword limit: int, optional - The maximum number of transfer items to return. The default value is 10
		:return: Returns a collection of transfer items.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		try:
			query_string = "?"
			if "sort_by" in kwargs:
				query_string.join("sortBy={0}&".format(kwargs["sort_by"]))
			if "start" in kwargs:
				query_string.join("start={0}&".format(kwargs["start"]))
			if "limit" in kwargs:
				query_string.join("limit={0}&".format(kwargs["limit"]))
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			res_query_string = lambda x: x if len(x) > 1 else x[:-1]

			api_path = "/analytic/transfers{0}".format(res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_transfer_item(self, transfer_id: str) -> requests.Response:
		"""
		Return a transfer result by ID
		:param transfer_id: required - Contains the transfer result ID
		:return: Returns a transfer result based on the ID that is specified in the path.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if transfer_id is None:
			raise Exception("Transfer ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/analytic/transfers/{0}".format(transfer_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def create_transfer_location(self, payload: dict) -> requests.Response:
		"""
		Generate a transfer location to upload analytic data
		:param payload: required - The JSON body that defines how the uploaded list is used
		:return: Creates a new transfer location that you can use to upload a file. The uploaded file must match the data descriptor in the request body. You can use this resource to define either which products are approved for use in recommendation tasks or which products are excluded from use in recommendation tasks.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		try:
			action = "POST"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/analytic/transfers"
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	AnalyticsServices()

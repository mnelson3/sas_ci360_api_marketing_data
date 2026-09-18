#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apimarketingdata.base import Base


class ImportRequestJobs(Base):
	"""
	Import Request Jobs Module
	Contains calls that create or retrieve requests to upload data to customer tables.
		1. get_import_requests(self, **kwargs) -> requests.Response
		2. create_import_request(self, payload: dict) -> requests.Response
		3. get_import_request(self, import_request_job_id: str) -> requests.Response
	"""

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_import_requests(self, **kwargs) -> requests.Response:
		"""
		Returns a summary of import requests
		:keyword data_descriptor_id: str, optional - Contains the ID of the data descriptor (customer table) that is associated with the import requests
		:keyword start: int, optional - Contains the first item to return
		:keyword limit: int, optional - Specifies the maximum number of items to return
		:return: Returns a summary of the import requests. Each returned summary object contains metadata that describes an import request.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		try:
			query_string = "?"
			if "data_descriptor_id" in kwargs:
				query_string.join("dataDescriptorId={0}&".format(kwargs["data_descriptor_id"]))
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
			api_path = "/importRequestJobs{0}".format(res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def create_import_request(self, payload: dict) -> requests.Response:
		"""
		Create and run an import request
		:param payload: required - Contains the JSON code to generate the import request job
		:return: Creates a job that processes uploaded data for a customer table. The import request processes an import file that you uploaded to a temporary URL (with the /marketingData/fileTransferLocation endpoint).
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
			api_path = "/importRequestJobs"
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_import_request(self, import_request_job_id: str) -> requests.Response:
		"""
		Returns an import request by job ID
		:param import_request_job_id: required - Contains the unique ID associated with the import request
		:return: Returns a specific import request based on the ID of the request job. The response contains a JSON representation of import request that describes an attempt to import table data from a temporary location.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if import_request_job_id is None:
			raise Exception("Import Request Job ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/importRequestJobs/{0}".format(import_request_job_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	ImportRequestJobs()

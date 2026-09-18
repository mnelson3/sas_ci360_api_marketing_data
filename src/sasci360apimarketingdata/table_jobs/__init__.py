#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apimarketingdata.base import Base


class TableJobs(Base):
	"""
	Table Jobs Module
	Contains calls to create, retrieve, or update data for a table.
		1. get_table_job(self, table_job_id: str) -> requests.Response
		2. create_table_job(self, payload: dict) -> requests.Response
	"""

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_table_job(self, table_job_id: str) -> requests.Response:
		"""
		Return a specific table job by ID
		:param table_job_id: required - Contains the unique ID that is associated with the table job
		:return: Returns an existing table job based on the ID in the path.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if table_job_id is None:
			raise Exception("Table Job ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/tableJobs/{0}".format(table_job_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def create_table_job(self, payload: dict) -> requests.Response:
		"""
		Create a table job
		:param payload: required - Contains the object with the information that is necessary to generate and run a job for a customer table
		:return: Creates and runs a table job.
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
			api_path = "/tableJobs"
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	TableJobs()

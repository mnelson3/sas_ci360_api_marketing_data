#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apimarketingdata.base import Base


class CustomerJobs(Base):
	"""
	Customer Jobs Module
	Contains calls that create, change, move, or delete customer information. These calls are used for GDPR requests.
		1. get_customer_job(self, customer_job_id: str) -> requests.Response
		2. create_customer_job(self, payload: dict) -> requests.Response
	"""

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_customer_job(self, customer_job_id: str) -> requests.Response:
		"""
		Return a customer job by ID
		:param customer_job_id: required - Contains the unique ID associated with this object
		:return: Returns a customer job based on the ID that is specified.
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
			api_path = "/customerJobs/{0}".format(customer_job_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def create_customer_job(self, payload: dict) -> requests.Response:
		"""
		Create and run a customer job
		:param payload: required - Contains the object with the request to import the file and the data description
		:return: Create a customer job that targets a specific customer or targets the data associated with the customer.
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
			api_path = "/customerJobs"
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	CustomerJobs()

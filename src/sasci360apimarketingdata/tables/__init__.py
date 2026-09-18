#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apimarketingdata.base import Base


class Tables(Base):
	"""
	Tables Module
	Contains calls that return information for existing tables.
		1. get_tables(self, **kwargs) -> requests.Response
		2. get_table(self, table_id: str) -> requests.Response
		3. create_table(self, payload: dict) -> requests.Response
		4. update_table(self, table_id: str, payload: dict) -> requests.Response
		5. delete_table(self, table_id: str) -> requests.Response
	"""

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_tables(self, **kwargs) -> requests.Response:
		"""
		Return a summary of all tables
		:keyword start: int, optional - Contains the first item to return
		:keyword limit: int, optional - Specifies the maximum number of items to return
		:keyword name: str, optional - Specifies the name of the table to return. The parameter's value must match a table's name exactly
		:keyword type: str, optional - Specifies the type of tables to return
		:return: Returns a summary of tables in the system. Each entry that is returned describes an existing table with a JSON representation.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		try:
			query_string = "?"
			if "start" in kwargs:
				query_string.join("start={0}&".format(kwargs["start"]))
			if "limit" in kwargs:
				query_string.join("limit={0}&".format(kwargs["limit"]))
			if "name" in kwargs:
				query_string.join("name={0}&".format(kwargs["name"]))
			if "type" in kwargs:
				query_string.join("type={0}&".format(kwargs["type"]))
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			res_query_string = lambda x: x if len(x) > 1 else x[:-1]
			api_path = "/tables{0}".format(res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_table(self, table_id: str) -> requests.Response:
		"""
		Return a table object by ID
		:param table_id: required - Contains the unique ID that is associated with the table object
		:return: Returns an object that contains metadata that describes an existing table.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if table_id is None:
			raise Exception("Table ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/tables/{0}".format(table_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def create_table(self, payload: dict) -> requests.Response:
		"""
		Create a customer table
		:param payload: required
		:return: Creates a customer table based on the body of the JSON request. The JSON body defines properties of the table and the columns that it contains. For more information about how to define tables in JSON, see Manually Create and Import the JSON for a Customer Table in the Administration Guide.
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
				# "Accept": "application/vnd.sas.api+json",
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

	def update_table(self, table_id: str, payload: dict) -> requests.Response:
		"""
		Update a table by ID
		:param table_id: required - Contains the unique ID that is associated with this item
		:param payload: required
		:return: Updates a table from SAS Customer Intelligence 360 based on the ID that is specified.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if table_id is None:
			raise Exception("Table ID is missing.")
		try:
			action = "PATCH"
			data = payload
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/tableJobs/{0}".format(table_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def delete_table(self, table_id: str) -> requests.Response:
		"""
		Delete a table by ID
		:param table_id: required - Contains the unique ID that is associated with this object
		:return: Removes a table from SAS Customer Intelligence 360 based on the ID that is specified.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if table_id is None:
			raise Exception("Digital Asset ID is missing.")
		try:
			action = "DELETE"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/tables/{0}".format(table_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	Tables()

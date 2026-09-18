#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apimarketingdata.base import Base


class IdentityRecords(Base):
	"""
	Identity Records Module
	Contains calls that return identity record information.
		1. get_identity_record_by_filter(self, **kwargs) -> requests.Response
		2. get_identity_record(self, identity_record_id: str) -> requests.Response
	"""

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def get_identity_record_by_filter(self, **kwargs) -> requests.Response:
		"""
		Return an identity record by ID filter
		:keyword "identity filter type": str, required - An identity type that you are filtering on and the corresponding value. The parameter name must be one of these values: emailId, customerId, deviceId, loginId, identityId, subjectId, or visitorId
		:return: Returns an identity record by the identity's type and the identity's value.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		try:
			query_string = "?"
			if "customer_id" in kwargs:
				query_string.join("customerId={0}&".format(kwargs["customer_id"]))
			elif "device_id" in kwargs:
				query_string.join("deviceId={0}&".format(kwargs["device_id"]))
			elif "email_id" in kwargs:
				query_string.join("emailId={0}&".format(kwargs["email_id"]))
			elif "identity_id" in kwargs:
				query_string.join("identityId={0}&".format(kwargs["identity_id"]))
			elif "login_id" in kwargs:
				query_string.join("loginId={0}&".format(kwargs["login_id"]))
			elif "subject_id" in kwargs:
				query_string.join("subjectId={0}&".format(kwargs["subject_id"]))
			elif "visitor_id" in kwargs:
				query_string.join("visitorId={0}&".format(kwargs["visitor_id"]))
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			res_query_string = lambda x: x if len(x) > 1 else x[:-1]
			api_path = "/identityRecords{0}".format(res_query_string(query_string))
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result

	def get_identity_record(self, identity_record_id: str) -> requests.Response:
		"""
		Return an identity record
		:param identity_record_id: required - Contains the unique ID that is associated with this object
		:return: Returns an identity record based on the specified ID. The response contains metadata that describes an existing identity in SAS Customer Intelligence 360.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		if identity_record_id is None:
			raise Exception("Identity Record ID is missing.")
		try:
			action = "GET"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/identityRecords/{0}".format(identity_record_id)
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	IdentityRecords()

#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

import requests
from sasci360apimarketingdata.base import Base


class FileTransferLocation(Base):
	"""
	File Transfer Location Module
	Contains a call to generate and return a signed URL. Use this URL to upload a file directly to a cloud storage location.
		1. create_file_transfer_location(self) -> requests.Response
	"""

	def __init__(self, algorithm, api, encoding, host, secret_key, tenant_id) -> None:
		super().__init__(algorithm, api, encoding, host, secret_key, tenant_id)

	def create_file_transfer_location(self) -> requests.Response:
		"""
		Create a signed URL to upload files
		:return: Creates and return an object containing a signed URL, to be used for secure file upload to a temporary location.
		:rtype: requests.Response
		"""
		result = None
		token = self.token
		api = self.api
		host = self.host
		try:
			action = "POST"
			data = None
			headers = {
				"Content-Type": "application/json",
				"Authorization": "Bearer {0}".format(token)
			}
			params = None
			api_path = "/fileTransferLocation"
			url = "https://{0}{1}{2}".format(host, api, api_path)
			result = self.connection.connect(action=action, data=data, headers=headers, params=params, url=url)
		except (AttributeError, Exception) as e:
			self.logger.exception("Exception occurred: {}".format(str(e)))
		finally:
			return result


if __name__ == "__main__":
	FileTransferLocation()

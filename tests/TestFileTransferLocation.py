#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
File Transfer Location Module
Contains a call to generate and return a signed URL. Use this URL to upload a file directly to a cloud storage location.
	1. create_file_transfer_location(self) -> requests.Response
"""

import os
import unittest
from sasci360apimarketingdata import file_transfer_location


class TestFileTransferLocation(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = "HS256"
		api = "/marketingData"
		encoding = "UTF-8"
		host = os.environ.get("CI360_HOST", "extapigwservice-prod.ci360.sas.com")
		secret_key = os.environ.get("CI360_SECRET_KEY", "changeme")
		tenant_id = os.environ.get("CI360_TENANT_ID", "changeme")

		self.file_transfer_location = file_transfer_location.FileTransferLocation(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_create_file_transfer_location(self):
		"""
		1. create_file_transfer_location(self) -> requests.Response
		"""
		result = self.file_transfer_location.create_file_transfer_location()
		print("Result: {}".format(result))
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()

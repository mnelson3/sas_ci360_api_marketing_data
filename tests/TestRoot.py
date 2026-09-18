#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Root Module
Contains the operations for the root resource.
	1. get_root(self) -> requests.Response
"""

import os
import unittest
from sasci360apimarketingdata import root


class TestRoot(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = "HS256"
		api = "/marketingData"
		encoding = "UTF-8"
		host = os.environ.get("CI360_HOST", "extapigwservice-prod.ci360.sas.com")
		secret_key = os.environ.get("CI360_SECRET_KEY", "changeme")
		tenant_id = os.environ.get("CI360_TENANT_ID", "changeme")

		self.root = root.Root(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_root(self):
		"""
		1. get_root(self) -> requests.Response
		"""
		result = self.root.get_root()
		print("Result: {}".format(result))
		print("Result: {}".format(result.status_code))
		print("Result: {}".format(result.json()))
		print("Result: {}".format(result.content))
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()

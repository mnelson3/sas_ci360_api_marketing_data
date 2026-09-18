#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Analytics Services Module
Contains the operations for the analytic services.
	1. get_analytics_services(self) -> requests.Response
	2. get_transfer_items(self, **kwargs) -> requests.Response
	3. get_transfer_item(self, transfer_id: str) -> requests.Response
	4. create_transfer_location(self, payload: dict) -> requests.Response
"""

import os
import unittest
from sasci360apimarketingdata import analytics_services


class TestAnalyticsServices(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = "HS256"
		api = "/marketingData"
		encoding = "UTF-8"
		host = os.environ.get("CI360_HOST", "extapigwservice-prod.ci360.sas.com")
		secret_key = os.environ.get("CI360_SECRET_KEY", "changeme")
		tenant_id = os.environ.get("CI360_TENANT_ID", "changeme")

		self.analytics_services = analytics_services.AnalyticsServices(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_analytics_services(self):
		"""
		1. get_analytics_services(self) -> requests.Response
		"""
		result = self.analytics_services.get_analytics_services()
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_transfer_items(self):
		"""
		2. get_transfer_items(self, **kwargs) -> requests.Response
		"""
		result = self.analytics_services.get_transfer_items()
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_transfer_item(self):
		"""
		3. get_transfer_item(self, transfer_id: str) -> requests.Response
		"""
		transfer_id = "0"
		result = self.analytics_services.get_transfer_item(transfer_id=transfer_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_create_transfer_location(self):
		"""
		4. create_transfer_location(self, payload: dict) -> requests.Response
		"""
		payload = {"columns": [{"length": 0, "name": "string", "type": "string"}], "listType": "allowlist"}
		result = self.analytics_services.create_transfer_location(payload=payload)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()

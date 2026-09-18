#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Tables Module
Contains calls that return information for existing tables.
	1. get_tables(self, **kwargs) -> requests.Response
	2. get_table(self, table_id: str) -> requests.Response
	3. create_table(self, payload: dict) -> requests.Response
	4. update_table(self, table_id: str, payload: dict) -> requests.Response
	5. delete_table(self, table_id: str) -> requests.Response
"""

import os
import unittest
from sasci360apimarketingdata import tables


class TestTables(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = "HS256"
		api = "/marketingData"
		encoding = "UTF-8"
		host = os.environ.get("CI360_HOST", "extapigwservice-prod.ci360.sas.com")
		secret_key = os.environ.get("CI360_SECRET_KEY", "changeme")
		tenant_id = os.environ.get("CI360_TENANT_ID", "changeme")

		self.tables = tables.Tables(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_tables(self):
		"""
		1. get_tables(self, **kwargs) -> requests.Response
		"""
		result = self.tables.get_tables()
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_table(self):
		"""
		2. get_table(self, table_id: str) -> requests.Response
		"""
		table_id = "0"
		result = self.tables.get_table(table_id=table_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_create_table(self):
		"""
		3. create_table(self, payload: dict) -> requests.Response
		"""
		payload = {
			"name": "sample_descriptor",
			"description": "customer tables",
			"type": "customer",
			"makeAvailableForTargeting": False,
			"dataItems": [
				{
					"name": "customer_id",
					"label": "Customer ID",
					"description": "Customer ID",
					"type": "STRING",
					"tags": ["DEMOGRAPHICS"],
					"identity": True,
					"key": True,
					"identityType": "customer_id",
					"excludeFromAnalytics": True
				},
				{
					"name": "email",
					"label": "email",
					"description": "email address",
					"type": "STRING",
					"tags": ["DEMOGRAPHICS", "EMAIL_CONTACT"],
					"excludeFromAnalytics": True,
					"identity": False,
					"segmentation": True
				},
				{
					"name": "gender",
					"label": "Gender",
					"description": "Gender",
					"type": "STRING",
					"tags": ["DEMOGRAPHICS"],
					"excludeFromAnalytics": True,
					"identity": False,
					"predefinedValues": ["M", "F"],
					"segmentProfilingField": True,
					"segmentation": True,
					"uniqueValuesAvailable": True
				},
				{
					"name": "age",
					"label": "Age",
					"description": "Age",
					"type": "INT",
					"tags": ["DEMOGRAPHICS"],
					"excludeFromAnalytics": True,
					"identity": False,
					"segmentation": True
				},
				{
					"name": "purchasedate",
					"label": "Recent Purchase Date",
					"description": "Recent Purchase Date",
					"type": "TIMESTAMP",
					"tags": ["DEMOGRAPHICS"],
					"identity": False,
					"excludeFromAnalytics": True,
					"segmentation": True
				},
				{
					"name": "purchasevalue",
					"label": "Recent Purchase Value",
					"description": "Recent Purchase Value",
					"type": "DOUBLE",
					"tags": ["DEMOGRAPHICS"],
					"identity": False,
					"excludeFromAnalytics": True,
					"segmentation": True
				},
				{
					"name": "emailok",
					"label": "Email is approved",
					"description": "customer can receive emails",
					"type": "STRING",
					"tags": ["DEMOGRAPHICS", "EMAIL_CONTACT"],
					"excludeFromAnalytics": True,
					"customProperties": [],
					"predefinedValues": [],
					"identity": False,
					"key": False,
					"segmentProfilingField": False,
					"uniqueValuesAvailable": False,
					"segmentation": False,
					"channelContactInformation": True,
					"identityAttribute": False
				}
			]
		}
		self.assertIsNotNone(self.tables.create_table(payload=payload))

	def test_update_table(self):
		"""
		4. update_table(self, table_id: str, payload: dict) -> requests.Response
		"""
		table_id = "0"
		payload = {
			"name": "sample_descriptor",
			"description": "customer tables",
			"type": "customer",
			"makeAvailableForTargeting": False,
			"dataItems": [
				{
					"name": "customer_id",
					"label": "Customer ID",
					"description": "Customer ID",
					"type": "STRING",
					"tags": ["DEMOGRAPHICS"],
					"identity": True,
					"key": True,
					"identityType": "customer_id",
					"excludeFromAnalytics": True
				},
				{
					"name": "email",
					"label": "email",
					"description": "email address",
					"type": "STRING",
					"tags": ["DEMOGRAPHICS", "EMAIL_CONTACT"],
					"excludeFromAnalytics": True,
					"identity": False,
					"segmentation": True
				},
				{
					"name": "gender",
					"label": "Gender",
					"description": "Gender",
					"type": "STRING",
					"tags": ["DEMOGRAPHICS"],
					"excludeFromAnalytics": True,
					"identity": False,
					"predefinedValues": ["M", "F"],
					"segmentProfilingField": True,
					"segmentation": True,
					"uniqueValuesAvailable": True
				},
				{
					"name": "age",
					"label": "Age",
					"description": "Age",
					"type": "INT",
					"tags": ["DEMOGRAPHICS"],
					"excludeFromAnalytics": True,
					"identity": False,
					"segmentation": True
				},
				{
					"name": "purchasedate",
					"label": "Recent Purchase Date",
					"description": "Recent Purchase Date",
					"type": "TIMESTAMP",
					"tags": ["DEMOGRAPHICS"],
					"identity": False,
					"excludeFromAnalytics": True,
					"segmentation": True
				},
				{
					"name": "purchasevalue",
					"label": "Recent Purchase Value",
					"description": "Recent Purchase Value",
					"type": "DOUBLE",
					"tags": ["DEMOGRAPHICS"],
					"identity": False,
					"excludeFromAnalytics": True,
					"segmentation": True
				},
				{
					"name": "emailok",
					"label": "Email is approved",
					"description": "customer can receive emails",
					"type": "STRING",
					"tags": ["DEMOGRAPHICS", "EMAIL_CONTACT"],
					"excludeFromAnalytics": True,
					"customProperties": [],
					"predefinedValues": [],
					"identity": False,
					"key": False,
					"segmentProfilingField": False,
					"uniqueValuesAvailable": False,
					"segmentation": False,
					"channelContactInformation": True,
					"identityAttribute": False
				}
			]
		}
		result = self.tables.update_table(table_id=table_id, payload=payload)
		self.assertIsNotNone(result)

	def test_delete_table(self):
		"""
		5. delete_table(self, table_id: str) -> requests.Response
		"""
		table_id = "0"
		result = self.tables.delete_table(table_id=table_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()

#! /usr/local/bin/python3
# -*- mode: python ; coding: utf-8 -*-

"""
Identity Records Module
Contains calls that return identity record information.
	1. get_identity_record_by_filter(self, **kwargs) -> requests.Response
	2. get_identity_record(self, identity_record_id: str) -> requests.Response
"""

import os
import unittest
from sasci360apimarketingdata import identity_records


class TestIdentityRecords(unittest.TestCase):

	def setUp(self) -> None:
		algorithm = "HS256"
		api = "/marketingData"
		encoding = "UTF-8"
		host = os.environ.get("CI360_HOST", "extapigwservice-prod.ci360.sas.com")
		secret_key = os.environ.get("CI360_SECRET_KEY", "changeme")
		tenant_id = os.environ.get("CI360_TENANT_ID", "changeme")

		self.identity_records = identity_records.IdentityRecords(
			algorithm=algorithm,
			api=api,
			encoding=encoding,
			host=host,
			secret_key=secret_key,
			tenant_id=tenant_id
		)

	def test_get_identity_record_by_filter_customer_id(self):
		"""
		1. get_identity_record_by_filter(self, **kwargs) -> requests.Response
		"""
		customer_id = "0"
		result = self.identity_records.get_identity_record_by_filter(customer_id=customer_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_identity_record_by_filter_device_id(self):
		"""
		1. get_identity_record_by_filter(self, **kwargs) -> requests.Response
		"""
		device_id = "0"
		result = self.identity_records.get_identity_record_by_filter(device_id=device_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_identity_record_by_filter_email_id(self):
		"""
		1. get_identity_record_by_filter(self, **kwargs) -> requests.Response
		"""
		email_id = "0"
		result = self.identity_records.get_identity_record_by_filter(email_id=email_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_identity_record_by_filter_identity_id(self):
		"""
		1. get_identity_record_by_filter(self, **kwargs) -> requests.Response
		"""
		identity_id = "0"
		result = self.identity_records.get_identity_record_by_filter(identity_id=identity_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_identity_record_by_filter_login_id(self):
		"""
		1. get_identity_record_by_filter(self, **kwargs) -> requests.Response
		"""
		login_id = "0"
		result = self.identity_records.get_identity_record_by_filter(login_id=login_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_identity_record_by_filter_subject_id(self):
		"""
		1. get_identity_record_by_filter(self, **kwargs) -> requests.Response
		"""
		subject_id = "0"
		result = self.identity_records.get_identity_record_by_filter(subject_id=subject_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_identity_record_by_filter_visitor_id(self):
		"""
		1. get_identity_record_by_filter(self, **kwargs) -> requests.Response
		"""
		visitor_id = "0"
		result = self.identity_records.get_identity_record_by_filter(visitor_id=visitor_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)

	def test_get_identity_record(self):
		"""
		2. get_identity_record(self, identity_record_id: str) -> requests.Response
		"""
		identity_record_id = "0"
		result = self.identity_records.get_identity_record(identity_record_id=identity_record_id)
		print("Result: {}".format(result))
		self.assertIsNotNone(result)


if __name__ == "__main__":
	unittest.main()
